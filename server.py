from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
# import docker
import requests
import json
import os
from flask import jsonify
from flask import Response
import time,datetime

# client = docker.from_env()
# client = docker.DockerClient(base_url='tcp://106.104.114.80:2375')
# client = docker.DockerClient(base_url='tcp://106.104.114.80:2375')


@app.route('/')
def index():
#     return 'Index Page'
	# return redirect(url_for('hello', username=request.form.get('username')))
	return redirect(url_for('static', filename='index.html'))

    # return render_template('black_cool_python3/index.html')

#註冊 node server 事件
# 建立連線用 docker ssh container
# json:{
# “USER_NAME”:”NULL”,
# “NODE_USER_ID”:”NULL”,
# “NODE_USER_ PASSWORD”:”NULL”,
# “NODE_NAME”:”NULL”,
# }
@app.route('/initnode',methods=['POST'])
def initnode():
    # 接收前端發來的資料,轉化為Json格式,我個人理解就是Python裡面的字典格式
    data = json.loads(request.get_data())
    email  = data["USER_EMAIL"]
    user = data["USER_NAME"]
    id = data["NODE_USER_ID"]
    pw = data["NODE_USER_PASSWORD"]
    name = data["NODE_NAME"]
    # data["time"] = "2016"
    # return 'The initnode json page'
    # Output: {u'age': 23, u'name': u'Peng Shuang', u'location': u'China'}
    # print data
    

    create_docker_config(data)
    # mail(data)
    print(user,id,email,pw,name)
    return jsonify(data)




def create_docker_config(data):
    
    docker_data = {
    	"Labels": {
    	    "email": data["USER_EMAIL"],
            "user": data["USER_NAME"],
            "id": data["NODE_USER_ID"],
            "pw": data["NODE_USER_PASSWORD"],
            "name": data["NODE_NAME"]
    	},
    	"Image": "gotechnies/alpine-ssh",
    	"HostConfig": {
    		"PortBindings": {
    			"22/tcp": [
    				{ "HostPort": "2222" }
    			],
    			"2375/tcp": [
    			    { "HostPost": "4444" }
    			]
    		}	
    	}
    }
    
    r = requests.post('http://13.78.29.239:2375/containers/create?name=test_container_'+data["NODE_NAME"] +str(int(time.mktime(datetime.datetime.today().timetuple()))),json=docker_data)
    return json.dumps(docker_data)


# print(create_docker_config({
#   "USER_NAME": "fixiabis",
#   "USER_EMAIL": "fixiabis@gmail.com",
#   "NODE_USER_ID": "hash_id",
#   "NODE_USER_PASSWORD": "password",
#   "NODE_NAME": "node"
# }))

def mail(data):
    # request.json 只能够接受方法为POST、Body为raw，header 内容为 application/json类型的数据：对应图1
    # json.loads(request.dada) 能够同时接受方法为POST、Body为 raw类型的 Text
    # 或者 application/json类型的值：对应图1、2
    # params = request.json if request.method == "POST" else request.args
    # try:
    #     data=params['name']
    #     print(data)

    # # except Exception, e:
    # #     logging.exception(e)
    # return jsonify(code=200, status=0, message='ok', data={})
    # #return 'Hello World!'
    print (request.is_json)
    content = request.get_json(silent = True)
    print (content["COMPANY"])
    print (content["MESSAGE"])
    print (content["NAME"])
    print (content["MAIL"])


    os.system("echo "+data["NODE_NAME"]+"訊息"+ data["NODE_USER_PASSWORD"]+"名稱"+data["USER_NAME"]+ " | ssmtp sddivid@gmail.com")

    print (content)
    return ('JSON posted')







@app.route('/containers/<string:port_id>')
def containers(port_id,):
    node_url='http://106.104.114.80:2375/containers/json'
    print(port_id)
    # try:
    #     r = requests.get(node_url)
    # except requests.ConnectionError as e:
    #     print ("url connect failed!")
    #     return "TAT"
    # else:
    r = requests.get(node_url)
    
    versionInfoPython = json.loads(r.text)

    print(versionInfoPython[0]['Id'])
    containers_list=list(map(lambda info: info['Id'], versionInfoPython))
    info=containers_list
    print(info)
    data_T = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
    }
 
    data = [versionInfoPython,data_T]
    print(data[1])
    
    # return '%s The containers page Post %s' %(info, port_id ) 
    return json.dumps(data)


@app.route('/start')
def start():
    # print(client.containers.get('edcf9a4213').labels)s
    return 'The about page'

@app.route('/restart')
def restart():
    # print(client.containers.get('edcf9a4213').labels)s
    return 'The about page'

@app.route('/stop')
def stop():
    # print(client.containers.get('edcf9a4213').labels)s
    return 'The about page'



@app.route('/about')
def about():
    return 'The about page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/HW')
def hello_world():
    return 'Hello World!'


@app.route('/HT')
def ht():
    return 'Hello HT!'

@app.route('/AC')
def ac():
    return 'Hello AC!'

@app.route('/door')
def door():
    return 'Hello door!'

@app.route('/HTD/<ht>')
def show_user_profile(ht):
    # show the user profile for that user
    return 'User %s' % ht

@app.route('/post/<string:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %s' % post_id

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()





if __name__ == '__main__':
    #app.run()
    app.debug = True
    app.run(host='0.0.0.0')
    # app.run(host='13.78.29.239')

