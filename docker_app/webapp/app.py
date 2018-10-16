import sys
import os
import socket
import cv2
import tensorflow as tf
import time
import keras
# from tensorflow import keras
from keras.models import load_model
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from flask import Flask
from flask import request
from redis import Redis, RedisError
from werkzeug.utils import secure_filename

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

globalPath = {
	'win_upload_path':r'D:\docker_app\webapp\uploads',
    'linux_upload_path':r'/app/uploads'
}

def evaluateImage(image_path):
    keras.backend.clear_session() 
    new_model = keras.models.load_model('/app/models/my_model.h5')
    # new_model.summary()

    raw_image = cv2.imread(image_path, 0)
    img = cv2.resize(raw_image,(28,28),interpolation=cv2.INTER_CUBIC)
    img = img.reshape(-1, 784) / 255.0
    # img = (img.reshape(-1,784)).astype("float32")/255
    predict = new_model.predict_classes(img)
    # cv2.imshow("Image1", raw_image)
    # cv2.waitKey(0)
    print("image:{0} is {1}".format(image_path, predict))
    return str(img), int(predict)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	# upload file to the server
    if request.method == 'POST':
        f = request.files['the_file']
        save_filename = globalPath['linux_upload_path']+'/'+secure_filename(f.filename)
        f.save(save_filename)
        return save_filename

# @app.route('/eval', methods=['POST'])
# def eval_image():
#     # upload file to the server
#     if request.method == 'POST':
#         t = time.time()
#         time_filename = "{0}.{1}".format(str(t), 'jpg')
#         f = request.files['the_file']
#         save_filename = globalPath['win_upload_path']+'\\'+time_filename
#         f.save(save_filename)
#         return evaluateImage(save_filename)

@app.route('/eval/image', methods=['POST'])
def eval_image_and_save():
    # upload file to the server
    if request.method == 'POST':
        t = time.time()
        time_filename = "{0}.{1}".format(str(t), 'jpg')
        f = request.files['the_file']
        save_filename = globalPath['linux_upload_path']+'/'+time_filename
        f.save(save_filename)
        graph_value, eval_value = evaluateImage(save_filename)

        rcd_time = time.time()
        sql_insert_rcd = 'INSERT INTO mnist_record (graph_value, eval_value, rcd_time) VALUES (\'{0}\', {1}, {2})'.format(graph_value, eval_value, str(int(rcd_time)))
        print(sql_insert_rcd)
        cluster = Cluster(['db'], port=9042)
        session = cluster.connect('mnistkeyspace')
        # query_res = session.execute('select * from mnist_record')
        # res_list = []
        # for res in query_res:
        #     print(res)
        #     res_list.append(res)
        session.execute(sql_insert_rcd)
        return eval_value

@app.route("/test")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

@app.route('/init')
def init_cassandra():
    # cluster = Cluster(['127.0.0.1'], load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='US_EAST'), port=8000)
    sql_create_ks = 'CREATE KEYSPACE mnistkeyspace WITH REPLICATION = { \'class\' : \'SimpleStrategy\' , \'replication_factor\' : 1 };'
    sql_use_ks = 'USE mnistkeyspace;'
    sql_create_table = 'CREATE TABLE mnist_record(graph_value text, eval_value int, rcd_time timestamp, PRIMARY KEY((rcd_time), eval_value));'
    sql_insert_test = 'INSERT INTO mnist_record (graph_value, eval_value, rcd_time) VALUES (\'000000\', 2, 140002827);'

    cluster = Cluster(['db'], port=9042)
    # cluster = Cluster()
    session = cluster.connect()
    session.execute(sql_create_ks)
    session.execute(sql_use_ks)
    session.execute(sql_create_table)
    session.execute(sql_insert_test)
    return 'init finished'

@app.route('/query')
def query_cassandra():
    # cluster = Cluster(['127.0.0.1'], load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='US_EAST'), port=8000)
    cluster = Cluster(['db'], port=9042)
    # cluster = Cluster()
    session = cluster.connect('mnistkeyspace')
    query_res = session.execute('select * from mnist_record')
    res_list = []
    for res in query_res:
        print(res)
        res_list.append(res)
    return str(res_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)