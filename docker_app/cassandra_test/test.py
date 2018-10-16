from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from flask import Flask
from flask import request
from werkzeug.utils import secure_filename

cluster = Cluster(['127.0.0.1'], port=8000)
session = cluster.connect('mnistkeyspace')
query_res = session.execute('select * from mnist_record')
res_list = []
for res in query_res:
	print(res)
	res_list.append(res)
# return res_list