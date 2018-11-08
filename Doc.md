<!-- ![test](https://raw.githubusercontent.com/imdonnie/playground/master/Markdown-Images/GitHub�?人�?�页.png) -->

#

<!-- TOC -->

- [1. 技�?栈和架构简�?](#1-技�?栈和架构简�?)
- [2. 文档内�??](#2-文�内�??)
- [3. Flask和接口调�?](#3-flask和接口调�?)
    - [3.1. �?速开�?](#31-�?速开�?)
    - [3.2. �?由绑�?](#32-�?由绑�?)
    - [3.3. 数据交互](#33-数据交互)
    - [3.4. 接口调试](#34-接口调试)
- [4. Cassandra���ݿ�](#4-cassandra���ݿ�)
    - [4.1. δ���](#41-δ���)
- [5. Dockerѧϰ��ʹ��](#5-dockerѧϰ��ʹ��)
    - [5.1. ��������](#51-��������)
- [4. Docker学习和使�?](#4-docker学习和使�?)
    - [4.1. 概念理解](#41-概念理��)
    - [5.2. Dockerfile��Container](#52-dockerfile��container)
    - [4.2. Dockerfile和Container](#42-dockerfile和Container)
    - [5.3. ����Container�����ͼ�Ⱥ����](#53-����container�����ͼ�Ⱥ����)
    - [4.3. 更�?�Container操作](#43-更�?�Container操作)
    - [5.4. ������������](#54-������������)
    - [5.5. Docker����](#55-docker����)

<!-- /TOC -->

# 1. 技�?栈和架构简�?

# 2. 文档内�??

# 3. Flask和接口调�?

## 3.1. �?速开�?

首先，从项目�?最直�?�的部分开始，也就是Flask的安装和配置。[Flask项目的官网](flask.pocco.org)已经对安装和配置做了很�?�细的�?�明。�?�果真的遇到什么问题，网上关于Flask的教程也很丰富。因此只要Python�?境没什么问题，Flask很快就可以安装完成，基本上安装就�?几�?�命令就ok了，当然速度不一定很�?。官网给出的安�?�命令�?�下�?

```Shell
$ pip install flask
 * flask is installed
```

这里的hello.py在官网上也给出了[源代码](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application)，很简单的一段：

```Python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

按照官网给出的方式运行：

```shell
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

显示已经运�?�在了本机的5000�?口上，至�?Flask的环境�?�置完成，并能�?�常运�?�。需要注意的一点是，由于我�?在windows�?境下进�?�的开发，所以并不能直接使用`export`命令对环境变量进行�?�置，不过不用担心，官网已经给出了windows下应该�?�何设置�?境变量的指�?�：

```Python
If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:
  C:\path\to\app>set FLASK_APP=hello.py
And on PowerShell:
  PS C:\path\to\app> $env:FLASK_APP = "hello.py"
```

最后补充一点，虽然官网上给出启动Flask的方法是先�?�置FLASK_APP�?境变量，然后再run，但�?这样其实并不�?很方便，我的做法�?直接在源代码最下面加上main函数作为入口�?

```Python
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

这样直接运�?�源代码就ok了：

```Shell
D:\github_repos\mnist_service\docker_app\webapp> python app.py

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
```

## 3.2. �?由绑�?

Flask的安装已经基�?完成了，但是最终项�?要实现的功能显然不是hello.py这么简单，因�?�以及往下看文档，�??一�?比较重�?�的部分就是**�?�?**，这�?概念其实很简单，�?以直接理解成�?**�?�?**和一�?**动作**绑定起来，以官网上给出的代码为例�?

```Python
@app.route('/hello')
def hello():
    return 'Hello, World'
```

这一段就�?�?'/hello'这一�?径和hello()函数进�?�了绑定，这样当用户访问``127.0.0.1:80/hello``时，就会触发`hello()`函数，也就是会返�?'Hello�? World'这个字�?�串。理解了这�??**绑定**逻辑，那么用�?由能实现�?些功能就完全�?由了，你�?以返回一段字符串、一�?特定格式的报文、一�?漂亮的网页或者在服务器的后台处理一堆数�?等等，至于具体的�?由使用文档，[Flask的文�?](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application)也写得很详细，一步�??follow一遍就基本熟悉了�?

## 3.3. 数据交互

基本了解了路由的绑定和使用之后，接下来就要�?��?�核心的后台逻辑了（毕竟�?项目没有要求漂亮的网页�?��?�），继�?阅�?�文档，在Flask�?，�?�求作为一�?对象�?处理，这�?对象包含了很多方法和属性，因�?�也不需要展开了解，文档中给出的例子已经足够我�?理解了：

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

阅�?�并能适当�?改这一段代码，基本上request的一些基�?用法就已经ok了，完整的request类中包含的方法和属性可以直接查看[request类的API文档](http://flask.pocoo.org/docs/1.0/api/#incoming-request-data)

## 3.4. 接口调试

最后�?�一点基于之前网页开发的建�??，由于项�?�?会涉及到文件上传这�?�操作，所以在调试的过程中�?定需要反复的上传文件或者提交表单，这样如果直接用浏览器来进行调试（比�?�在Google Chrome�?按F12），�?能构造测试数�?的过程会很�?�杂，而且也有很�?�的限制。因此我在调试的过程�?用到了[Postman](https://www.getpostman.com/)，这�?一�?用于接口调试（不仅仅限于网页）的工具，借助Postman�?以很容易地构造各种http报文，包括Get、Post方法的选择、提交文件、构造�?�杂表单、构造http头等等，最后放一张Postman的表单构造器�?图，还是很强大的�?
![Postman构造表单](https://raw.githubusercontent.com/imdonnie/playground/master/Markdown-Images/Postman构造表�?.png)

<<<<<<< HEAD
# 4. Cassandra���ݿ�

## 4.1. δ���

# 5. Dockerѧϰ��ʹ��

## 5.1. ��������
=======
# 4. Docker学习和使�?

## 4.1. 概念理解
>>>>>>> be94bbce0f2d3b0f440464b1f66483df89f5d51c

如果说�?�于有一定Python基�?�的人来�?�，写出一�?简单的Flask应用�?能只�?一两个小时的事情，那么Docker显然没有这么容易，其�?各�?��?�念、逻辑甚至�?哲�?�都�?能成为运用Docker的阻碍�?
仍然�?从[文档](https://docs.docker.com/get-started/)开始。�??一部分主�?�是对Docker的�?��?�目的的介绍，同时也引出了一些基�?的�?�念。引用一段Docker原文的�?�解�?
> A container is launched by running an image. An image is an executable package that includes everything needed to run an application--the code, a runtime, libraries, environment variables, and configuration files.
> A container is a runtime instance of an image--what the image becomes in memory when executed (that is, an image with state, or a user process). You can see a list of your running containers with the command, docker ps, just as you would in Linux.

<<<<<<< HEAD
���⣺image����Ծ�̬�ģ�����������һ��app��Ҫ�Ĵ�������������ƿ�ִ���ļ��������ļ��ļ��ϣ���image��������ʱ�������ڴ�ʱ����Ϊһ��container�����ƽ��̡�
=======
理解：image�?相�?�静态的，包�?了运行一个app需要的代码和依赖，类似�?执�?�文件和配置文件的集合；当image运�?�起来时（放入内存时）成为一个container，类似进程�?
>>>>>>> be94bbce0f2d3b0f440464b1f66483df89f5d51c

接着往下看�?
>Containerization makes CI/CD seamless. For example:
>
>- applications have no system dependencies
>- updates can be pushed to any part of a distributed application
>- resource density can be optimized.

<<<<<<< HEAD
���⣺����docker��һЩ�ô���Ӧ�������ϵͳ����ͣ����ڳ������ɺͳ����������Ż���Դ���á�**����ĿΪ�˼�����image�Ĺ��̣����DockerHub��GitHub������һ���򵥵ĳ������ɷ��񣬾���ʵ�ַ�����֮����½ڡ�**

## 5.2. Dockerfile��Container
=======
?理解：利用docker的一些好处，应用与操作系统解耦和，便于持�?集成和持�?发布，优化资源配�?�?**�?项目为了简化生成image的过程，结合DockerHub和GitHub配置了一�?简单的持续集成服务，具体实现方法�?�之后的章节�?**

## 4.2. Dockerfile和Container
>>>>>>> be94bbce0f2d3b0f440464b1f66483df89f5d51c

�?二部分继�?介绍了一些�?�念以及这些概念之间的关系做了介绍：
>It’s time to begin building an app the Docker way. We start at the bottom of the hierarchy of such an app, which is a container, which we cover on this page. Above this level is a service, which defines how containers behave in production, covered in Part 3. Finally, at the top level is the stack, defining the interactions of all the services, covered in Part 5.

<<<<<<< HEAD
���⣺docker�ϵ�Ӧ�ò�Σ���ײ�Ϊcontainer�����ƽ��̣����ϲ�Ϊservice��������container��ι�����part3���ݣ������service�ѵ���stack��ͬʱstack������service֮��Ľ�����part5����
=======
理解：docker上的应用层�?�：最底层为container（类似进程），上层为service，定义了container如何工作（part3内�?�），�?�个service堆叠成stack，同时stack定义了service之间的交互（part5）�?
>>>>>>> be94bbce0f2d3b0f440464b1f66483df89f5d51c

接着，文档解释了Docker�?十分重�?�的内�?�：Dockerfile，并且给出了一�?简单的Dockerfile样例�?
>Dockerfile defines what goes on in the environment inside your container. Access to resources like networking interfaces and disk drives is virtualized inside this environment, which is isolated from the rest of your system, so you need to map ports to the outside world, and be specific about what files you want to “copy in�? to that environment. However, after doing that, you can expect that the build of your app defined in this Dockerfile behaves exactly the same wherever it runs.

`Dockerfile`

```Dockerfile
# Use an official Python runtime as a parent image
# 以一�?精简版的python-3�?境作为parent image（其他的改动都是基于这个镜像之上的）
FROM python:3-slim
# Set the working directory to /app
# 设定 /app 为工作路�?
WORKDIR /app
# Copy the current directory contents into the container at /app
# 将当前路径（源代码所在路径）拷贝进container�?�? /app�?径中
COPY . /app
# Install any needed packages specified in requirements.txt
# 根据requirements.txt�?的�?�求配置�?�?
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Make port 80 available to the world outside this container
# 将这个container�?80�?口暴露出�?
EXPOSE 80
# Define environment variable
# 定义一�?�?境变量，在这段代码中似乎没什么作�?，但�?之后会用到的
ENV NAME World
# Run app.py when the container launches
# 在container�?执�?? python app.py 这个命令
CMD ["python", "app.py"]
```

`requirements.txt`

```Plain Text
Flask
Redis
```

<<<<<<< HEAD
���⣺����һ�׶�Ҫ��ȫ������һ�ε�д�����ǱȽ����ѵģ����Խ�Ͻű��е�ע�ͣ���Ȼ�϶����������ʣ������⵽Dockerfile���ڶ���container������������ͬʱ����ӿ�ӳ�����Ϣ��requiremnets.txt��������python����Ҫ�Ŀ⣬�������㹻�ˡ�
=======
理解：在这一阶�?��?�完全理解这一段的写法还是比较困难的，�?以结合脚�?�?的注释（虽然�?定还�?有疑�?），理解到Dockerfile用于定义container的启动动作，同时定义接口映射等信�?，requiremnets.txt用于配置python�?需要的库，这样就足够了�?
>>>>>>> be94bbce0f2d3b0f440464b1f66483df89f5d51c

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

<<<<<<< HEAD
���⣺`app.py`����ûʲô̫���˵�ģ���Ҫ����һ������������ͨ��һ������������У�����Ҳ�ع���һ�µ�һ�¶�Flask�Ľ��ܡ�
=======
理解：`app.py`�?�?没什么太多可说的，主要就�?一�?测试用例，通�?�一遍理解清楚就行，正好也回顾了一下�??一章�?�Flask的介绍�?
>>>>>>> be94bbce0f2d3b0f440464b1f66483df89f5d51c

复制完上面这些代码后，就�?以按照文档的说明来试着跑一下�??一个Docker Container了，首先，类似Linux�?的Makefile，Dockerfile�?对一堆源代码进�?�编译的脚本文件，在配置好的Docker�?境，�?以直接命令�?�编译运行�?

首先�?认一下目录中的文件都齐了�?

```Shell
$ ls
Dockerfile app.py requirements.txt
```

然后一行命令直接编译：

```Shell
docker build -t friendlyhello .
```

编译完成后运行docker命令看一下：

```Shell
$ docker image ls

REPOSITORY            TAG                 IMAGE ID
friendlyhello         latest              326387cea398
```

看到friendlyhello已经成功编出来，那么Dockerfile这部分就基本ok了，接下来可以继�?参考文档，运�?�一下就行�?

<<<<<<< HEAD
## 5.3. ����Container�����ͼ�Ⱥ����
=======
## 4.3. 更�?�Container操作
>>>>>>> be94bbce0f2d3b0f440464b1f66483df89f5d51c

前文已经完成了一�?简单的Dockefile的编写，但是明显还有很�?�问题悬而未决，比�?�：应�?��?�何调试Container？�?�果程序运�?�的�?境比较�?�杂时可以用一个Dockerfile搞定么（比�?�Python+Tensorflow+Flask+Cassandra...）？不同的Container之间如果同时运�?�，那么它们之间应�?��?�何交互�?？这些问题可能在这一节无法全部解决，但是这都�?要完成项�?所无法绕开的�?

首先结合Docker的官方文档，�?以进一步了�?docker-compose.yml�?
>A docker-compose.yml file is a YAML file that defines how Docker containers should behave in production.

<<<<<<< HEAD
���⣺docker-compose.yml���ڿ���containerӦ��������У�Ҳ���ǽ�container��װ��service�����߿��Խ���**��������**���������ĵ��и��������ӣ�
=======
理解：docker-compose.yml用于控制container应�?��?�何运�?�，也就�?将container包�?�成service，或者可以叫�?**容器编排**，下面是文档�?给出的例子：
>>>>>>> be94bbce0f2d3b0f440464b1f66483df89f5d51c

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

文档�?对于这一段docker-compose.yml的解释：
>This docker-compose.yml file tells Docker to do the following:
>Pull the image we uploaded in step 2 from the registry.
>
>- Run 5 instances of that image as a service called web, limiting each one to use, at  most, 10% of the CPU (across all cores), and 50MB of RAM.
>- Immediately restart containers if one fails.
>- Map port 4000 on the host to web’s port 80.
>- Instruct web’s containers to share port 80 via a load-balanced network called webnet. (Internally, the containers themselves publish to web’s port 80 at an ephemeral port.)
>- Define the webnet network with the default settings (which is a load-balanced overlay network).

下面仍然�?一段操作指导，直接�?运原文了�?

运�?��?��?�：

```Shell
docker swarm init
docker stack deploy -c docker-compose.yml getstartedlab
```

>Our single service stack is running 5 container instances of our deployed image on one host. Let’s investigate.
>Get the service ID for the one service in our application:
`docker service ls`
>Look for output for the web service, prepended with your app name. If you named it the same as shown in this example, the name isgetstartedlab_web. The service ID is listed as well, along with the number of replicas, image name, and exposed ports.
>A single container running in a service is called a task. Tasks are given unique IDs that numerically increment, up to the number of replicas you defined in docker-compose.yml. List the tasks for your service:
`docker service ps getstartedlab_web`
>Tasks also show up if you just list all the containers on your system, though that is not filtered by service:
`docker container ls -q`
>关闭步�?�：
>Take the app down with docker stack rm:
`docker stack rm getstartedlab`
>Take down the swarm.
`docker swarm leave --force`

<<<<<<< HEAD
���⣺����״̬�µĶ�����stack>service>container(=running image)��or image+Dockerfile=container, container+docker-compose.yml=service
�ٴ�ǿ����Dockerfile������image����������������������������������кͱ���ָ�����Makefile����YAML������һ��container��������������Դռ�ã��˿�ӳ�䣬scale���ã����ؾ��⣬����һ����Դ���ȵ������ļ�����

������Ŀ������������Ҫ�Ļ���������Ҫ��һ��**��������˳���Flask+Tenforslow��** ����һ�� **���ݿ����Cassandra��**�����ҵ�ʵ�ֹ����У����������Ǻ����ںϵģ�Ҳ����˵����������Container�зֱ������������֣�����������֮���ܹ���ȷ��������Ϊ��Ŀ����Ҫ�����ݿ��д���ݣ���

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

���⣺docker-compose.yml����������service����ʵ��������container������ͬʱ����һЩ���ã���������ʽ���Լ����ǵ�����˳���Դ����ǿ����ٽ�һ������container����Ȼcontainer�Ǻ�������runtime��������os�����ǻ���Ӧ�ý�����Ϊһ�����̱ȽϺã����մ������������**����**����ĳһ����һ��container������**һ��container**��Э������ȱ����Ŀ���������һ��Web�������Ͽ�����Ҫ����Node.js��Apache��MySQL�ȵȣ���ÿһ��������Docker���߼��о�Ӧ����һ��Container��ʵ�֡�

������������Ż����漰���硢�������õȵȣ���˻�����Ҫ�Ķ�[Compose�ٷ��ĵ�������½�](https://docs.docker.com/compose/gettingstarted/)���ڴ˾Ͳ���׸���ˡ�

## 5.5. Docker����
=======
理解：运行状态下的�?�个概念，stack>service>container(=running image)，or image+Dockerfile=container, container+docker-compose.yml=service
再�?�强调，Dockerfile定义了image的启�?（比如加载依赖，�?境变量，运�?�和编译指令，类似Makefile），YAML定义了一组container的启�?（比如资源占�?，�??口映射，scale设置，负载均衡，类似一�?资源调度的配�?文件�?
>>>>>>> be94bbce0f2d3b0f440464b1f66483df89f5d51c
