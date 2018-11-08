<!-- ![test](https://raw.githubusercontent.com/imdonnie/playground/master/Markdown-Images/GitHub������ҳ.png) -->

#

<!-- TOC -->

- [1. ����ջ�ͼܹ����](#1-����ջ�ͼܹ����)
- [2. �ĵ�����](#2-�ĵ�����)
- [3. Flask�ͽӿڵ���](#3-flask�ͽӿڵ���)
    - [3.1. ���ٿ�ʼ](#31-���ٿ�ʼ)
    - [3.2. ·�ɰ�](#32-·�ɰ�)
    - [3.3. ���ݽ���](#33-���ݽ���)
    - [3.4. �ӿڵ���](#34-�ӿڵ���)
- [4. Cassandra���ݿ�](#4-cassandra���ݿ�)
    - [4.1. δ���](#41-δ���)
- [5. Dockerѧϰ��ʹ��](#5-dockerѧϰ��ʹ��)
    - [5.1. �������](#51-�������)
    - [5.2. Dockerfile��Container](#52-dockerfile��container)
    - [5.3. ����Container�����ͼ�Ⱥ����](#53-����container�����ͼ�Ⱥ����)
    - [5.4. ������������](#54-������������)
    - [5.5. Docker����](#55-docker����)

<!-- /TOC -->

# 1. ����ջ�ͼܹ����

# 2. �ĵ�����

# 3. Flask�ͽӿڵ���

## 3.1. ���ٿ�ʼ

���ȣ�����Ŀ����ֱ�۵Ĳ��ֿ�ʼ��Ҳ����Flask�İ�װ�����á�[Flask��Ŀ�Ĺ���](flask.pocco.org)�Ѿ��԰�װ���������˺���ϸ��˵��������������ʲô���⣬���Ϲ���Flask�Ľ̳�Ҳ�ܷḻ�����ֻҪPython����ûʲô���⣬Flask�ܿ�Ϳ��԰�װ��ɣ������ϰ�װ���Ǽ��������ok�ˣ���Ȼ�ٶȲ�һ���ܿ졣���������İ�װ�������£�

```Shell
$ pip install flask
 * flask is installed
```

�����hello.py�ڹ�����Ҳ������[Դ����](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application)���ܼ򵥵�һ�Σ�

```Python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

���չ��������ķ�ʽ���У�

```shell
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

��ʾ�Ѿ��������˱�����5000�˿��ϣ�����Flask�Ļ���������ɣ������������С���Ҫע���һ���ǣ�����������windows�����½��еĿ��������Բ�����ֱ��ʹ��`export`����Ի��������������ã��������õ��ģ������Ѿ�������windows��Ӧ��������û���������ָ����

```Python
If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:
  C:\path\to\app>set FLASK_APP=hello.py
And on PowerShell:
  PS C:\path\to\app> $env:FLASK_APP = "hello.py"
```

��󲹳�һ�㣬��Ȼ�����ϸ�������Flask�ķ�����������FLASK_APP����������Ȼ����run������������ʵ�����Ǻܷ��㣬�ҵ�������ֱ����Դ�������������main������Ϊ��ڣ�

```Python
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

����ֱ������Դ�����ok�ˣ�

```Shell
D:\github_repos\mnist_service\docker_app\webapp> python app.py

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
```

## 3.2. ·�ɰ�

Flask�İ�װ�Ѿ���������ˣ�����������ĿҪʵ�ֵĹ�����Ȼ����hello.py��ô�򵥣�����Լ����¿��ĵ�����һ���Ƚ���Ҫ�Ĳ��־���**·��**�����������ʵ�ܼ򵥣�����ֱ�����ɽ�**·��**��һ��**����**���������Թ����ϸ����Ĵ���Ϊ����

```Python
@app.route('/hello')
def hello():
    return 'Hello, World'
```

��һ�ξ��ǽ�'/hello'��һ·����hello()���������˰󶨣��������û�����``127.0.0.1:80/hello``ʱ���ͻᴥ��`hello()`������Ҳ���ǻ᷵��'Hello�� World'����ַ��������������**��**�߼�����ô��·����ʵ����Щ���ܾ���ȫ�����ˣ�����Է���һ���ַ�����һ���ض���ʽ�ı��ġ�һ��Ư������ҳ�����ڷ������ĺ�̨����һ�����ݵȵȣ����ھ����·��ʹ���ĵ���[Flask���ĵ�](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application)Ҳд�ú���ϸ��һ����followһ��ͻ�����Ϥ�ˡ�

## 3.3. ���ݽ���

�����˽���·�ɵİ󶨺�ʹ��֮�󣬽�������Ҫ��ƺ��ĵĺ�̨�߼��ˣ��Ͼ�����Ŀû��Ҫ��Ư������ҳ��ƣ��������Ķ��ĵ�����Flask�У�������Ϊһ�����󱻴��������������˺ܶ෽�������ԣ����Ҳ����Ҫչ���˽⣬�ĵ��и����������Ѿ��㹻��������ˣ�

```Python
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
```

�Ķ������ʵ��޸���һ�δ��룬������request��һЩ�����÷����Ѿ�ok�ˣ�������request���а����ķ��������Կ���ֱ�Ӳ鿴[request���API�ĵ�](http://flask.pocoo.org/docs/1.0/api/#incoming-request-data)

## 3.4. �ӿڵ���

���˵һ�����֮ǰ��ҳ�����Ľ��飬������Ŀ�л��漰���ļ��ϴ����ֲ����������ڵ��ԵĹ����п϶���Ҫ�������ϴ��ļ������ύ�����������ֱ��������������е��ԣ�������Google Chrome�а�F12�������ܹ���������ݵĹ��̻�ܸ��ӣ�����Ҳ�кܶ�����ơ�������ڵ��ԵĹ������õ���[Postman](https://www.getpostman.com/)������һ�����ڽӿڵ��ԣ�������������ҳ���Ĺ��ߣ�����Postman���Ժ����׵ع������http���ģ�����Get��Post������ѡ���ύ�ļ������츴�ӱ�������httpͷ�ȵȣ�����һ��Postman�ı���������ͼ�����Ǻ�ǿ��ģ�
![Postman�����](https://raw.githubusercontent.com/imdonnie/playground/master/Markdown-Images/Postman�����.png)

# 4. Cassandra���ݿ�

## 4.1. δ���

# 5. Dockerѧϰ��ʹ��

## 5.1. �������

���˵������һ��Python����������˵��д��һ���򵥵�FlaskӦ�ÿ���ֻ��һ����Сʱ�����飬��ôDocker��Ȼû����ô���ף����и��ָ���߼���������ѧ�����ܳ�Ϊ����Docker���谭��
��Ȼ�Ǵ�[�ĵ�](https://docs.docker.com/get-started/)��ʼ����һ������Ҫ�Ƕ�Docker�����Ŀ�ĵĽ��ܣ�ͬʱҲ������һЩ�����ĸ������һ��Dockerԭ�ĵĽ��⣺
> A container is launched by running an image. An image is an executable package that includes everything needed to run an application--the code, a runtime, libraries, environment variables, and configuration files.
> A container is a runtime instance of an image--what the image becomes in memory when executed (that is, an image with state, or a user process). You can see a list of your running containers with the command, docker ps, just as you would in Linux.

��⣺image����Ծ�̬�ģ�����������һ��app��Ҫ�Ĵ�������������ƿ�ִ���ļ��������ļ��ļ��ϣ���image��������ʱ�������ڴ�ʱ����Ϊһ��container�����ƽ��̡�

�������¿���
>Containerization makes CI/CD seamless. For example:
>
>- applications have no system dependencies
>- updates can be pushed to any part of a distributed application
>- resource density can be optimized.

��⣺����docker��һЩ�ô���Ӧ�������ϵͳ����ͣ����ڳ������ɺͳ����������Ż���Դ���á�**����ĿΪ�˼�����image�Ĺ��̣����DockerHub��GitHub������һ���򵥵ĳ������ɷ��񣬾���ʵ�ַ�����֮����½ڡ�**

## 5.2. Dockerfile��Container

�ڶ����ּ���������һЩ�����Լ���Щ����֮��Ĺ�ϵ���˽��ܣ�
>It��s time to begin building an app the Docker way. We start at the bottom of the hierarchy of such an app, which is a container, which we cover on this page. Above this level is a service, which defines how containers behave in production, covered in Part 3. Finally, at the top level is the stack, defining the interactions of all the services, covered in Part 5.

��⣺docker�ϵ�Ӧ�ò�Σ���ײ�Ϊcontainer�����ƽ��̣����ϲ�Ϊservice��������container��ι�����part3���ݣ������service�ѵ���stack��ͬʱstack������service֮��Ľ�����part5����

���ţ��ĵ�������Docker��ʮ����Ҫ�����ݣ�Dockerfile�����Ҹ�����һ���򵥵�Dockerfile������
>Dockerfile defines what goes on in the environment inside your container. Access to resources like networking interfaces and disk drives is virtualized inside this environment, which is isolated from the rest of your system, so you need to map ports to the outside world, and be specific about what files you want to ��copy in�� to that environment. However, after doing that, you can expect that the build of your app defined in this Dockerfile behaves exactly the same wherever it runs.

`Dockerfile`

```Dockerfile
# Use an official Python runtime as a parent image
# ��һ��������python-3������Ϊparent image�������ĸĶ����ǻ����������֮�ϵģ�
FROM python:3-slim
# Set the working directory to /app
# �趨 /app Ϊ����·��
WORKDIR /app
# Copy the current directory contents into the container at /app
# ����ǰ·����Դ��������·����������container�е� /app·����
COPY . /app
# Install any needed packages specified in requirements.txt
# ����requirements.txt�е�Ҫ�����û���
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Make port 80 available to the world outside this container
# �����container��80�˿ڱ�¶����
EXPOSE 80
# Define environment variable
# ����һ����������������δ������ƺ�ûʲô���ã�����֮����õ���
ENV NAME World
# Run app.py when the container launches
# ��container��ִ�� python app.py �������
CMD ["python", "app.py"]
```

`requirements.txt`

```Plain Text
Flask
Redis
```

��⣺����һ�׶�Ҫ��ȫ�����һ�ε�д�����ǱȽ����ѵģ����Խ�Ͻű��е�ע�ͣ���Ȼ�϶����������ʣ�����⵽Dockerfile���ڶ���container������������ͬʱ����ӿ�ӳ�����Ϣ��requiremnets.txt��������python����Ҫ�Ŀ⣬�������㹻�ˡ�

`app.py`

```Python
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

��⣺`app.py`����ûʲô̫���˵�ģ���Ҫ����һ������������ͨ��һ�����������У�����Ҳ�ع���һ�µ�һ�¶�Flask�Ľ��ܡ�

������������Щ����󣬾Ϳ��԰����ĵ���˵����������һ�µ�һ��Docker Container�ˣ����ȣ�����Linux�е�Makefile��Dockerfile�Ƕ�һ��Դ������б���Ľű��ļ��������úõ�Docker����������ֱ�������б������С�

����ȷ��һ��Ŀ¼�е��ļ������ˣ�

```Shell
$ ls
Dockerfile app.py requirements.txt
```

Ȼ��һ������ֱ�ӱ��룺

```Shell
docker build -t friendlyhello .
```

������ɺ�����docker���һ�£�

```Shell
$ docker image ls

REPOSITORY            TAG                 IMAGE ID
friendlyhello         latest              326387cea398
```

����friendlyhello�Ѿ��ɹ����������ôDockerfile�ⲿ�־ͻ���ok�ˣ����������Լ����ο��ĵ�������һ�¾��С�

## 5.3. ����Container�����ͼ�Ⱥ����

ǰ���Ѿ������һ���򵥵�Dockefile�ı�д���������Ի��кܶ���������δ�������磺Ӧ����ε���Container������������еĻ����Ƚϸ���ʱ������һ��Dockerfile�㶨ô������Python+Tensorflow+Flask+Cassandra...������ͬ��Container֮�����ͬʱ���У���ô����֮��Ӧ����ν����أ���Щ�����������һ���޷�ȫ������������ⶼ��Ҫ�����Ŀ���޷��ƿ��ġ�

���Ƚ��Docker�Ĺٷ��ĵ������Խ�һ���˽�docker-compose.yml��
>A docker-compose.yml file is a YAML file that defines how Docker containers should behave in production.

��⣺docker-compose.yml���ڿ���containerӦ��������У�Ҳ���ǽ�container��װ��service�����߿��Խ���**��������**���������ĵ��и��������ӣ�

`docker-compose.yml`

```YAML
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: username/repo:tag
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "4000:80"
    networks:
      - webnet
networks:
  webnet:
```

�ĵ��ж�����һ��docker-compose.yml�Ľ��ͣ�
>This docker-compose.yml file tells Docker to do the following:
>Pull the image we uploaded in step 2 from the registry.
>
>- Run 5 instances of that image as a service called web, limiting each one to use, at  most, 10% of the CPU (across all cores), and 50MB of RAM.
>- Immediately restart containers if one fails.
>- Map port 4000 on the host to web��s port 80.
>- Instruct web��s containers to share port 80 via a load-balanced network called webnet. (Internally, the containers themselves publish to web��s port 80 at an ephemeral port.)
>- Define the webnet network with the default settings (which is a load-balanced overlay network).

������Ȼ��һ�β���ָ����ֱ�Ӱ���ԭ���ˣ�

���в��裺

```Shell
docker swarm init
docker stack deploy -c docker-compose.yml getstartedlab
```

>Our single service stack is running 5 container instances of our deployed image on one host. Let��s investigate.
>Get the service ID for the one service in our application:
`docker service ls`
>Look for output for the web service, prepended with your app name. If you named it the same as shown in this example, the name isgetstartedlab_web. The service ID is listed as well, along with the number of replicas, image name, and exposed ports.
>A single container running in a service is called a task. Tasks are given unique IDs that numerically increment, up to the number of replicas you defined in docker-compose.yml. List the tasks for your service:
`docker service ps getstartedlab_web`
>Tasks also show up if you just list all the containers on your system, though that is not filtered by service:
`docker container ls -q`
>�رղ��裺
>Take the app down with docker stack rm:
`docker stack rm getstartedlab`
>Take down the swarm.
`docker swarm leave --force`

��⣺����״̬�µĶ�����stack>service>container(=running image)��or image+Dockerfile=container, container+docker-compose.yml=service
�ٴ�ǿ����Dockerfile������image����������������������������������кͱ���ָ�����Makefile����YAML������һ��container��������������Դռ�ã��˿�ӳ�䣬scale���ã����ؾ��⣬����һ����Դ���ȵ������ļ�����

������Ŀ����������Ҫ�Ļ���������Ҫ��һ��**��������˳���Flask+Tenforslow��** ����һ�� **���ݿ����Cassandra��**�����ҵ�ʵ�ֹ����У����������Ǻ����ںϵģ�Ҳ����˵����������Container�зֱ������������֣�����������֮���ܹ���ȷ��������Ϊ��Ŀ����Ҫ�����ݿ��д���ݣ���

������������������Ҫ��һ���˽�Docker�е�**��������**��

## 5.4. ������������

���ո�д���һ��Dockfileʱ������������Ŀ�������������ģ��Ͼ��Ѿ�������Docker�ż��ı�Ե�����Ǻܿ�ͷ�����һ���п����ʵ���Ǿ�����ΰѷ����������ݿ����õ�ͬһ���������������Python��parent image����������Cassandra��Ҳ�Թ���CassandraΪparent image������������python��������ʵ����Щ��������ȷ�İ취����������������ݿⲻ����д��ͬһ��Dockerfile�С���ʱ���ǹٷ��ĵ�����������
>Create a file called docker-compose.yml in your project directory and paste the following:

```YAML
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
  redis:
    image: "redis:alpine"
```

�������ƺ�ֻ�ж̶̼��У�������ʵ����Ѿ�����˵���Container�����޷��������飬�Ǿ�������������Զ����ķ���
>This Compose file defines two services, **web** and **redis**. The web service:
>
> - Uses an image that��s built from the Dockerfile in the current directory.
>
>- Forwards the exposed port 5000 on the container to port 5000 on the host machine. We use the default port for the Flask web server, 5000.
>
>The redis service uses a public Redis image pulled from the Docker Hub registry.

��⣺docker-compose.yml����������service����ʵ��������container������ͬʱ����һЩ���ã���������ʽ���Լ����ǵ�����˳���Դ����ǿ����ٽ�һ�����container����Ȼcontainer�Ǻ�������runtime��������os�����ǻ���Ӧ�ý�����Ϊһ�����̱ȽϺã����մ������������**����**����ĳһ����һ��container������**һ��container**��Э������ȱ����Ŀ���������һ��Web�������Ͽ�����Ҫ����Node.js��Apache��MySQL�ȵȣ���ÿһ��������Docker���߼��о�Ӧ����һ��Container��ʵ�֡�

������������Ż����漰���硢�������õȵȣ���˻�����Ҫ�Ķ�[Compose�ٷ��ĵ�������½�](https://docs.docker.com/compose/gettingstarted/)���ڴ˾Ͳ���׸���ˡ�

## 5.5. Docker����