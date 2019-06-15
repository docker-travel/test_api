from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
import docker
import requests
import json
from flask import jsonify
from flask import Response
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
    user = data["USER_NAME"]
    id = data["NODE_USER_ID"]
    pw = data["NODE_USER_PASSWORD"]
    name = data["NODE_NAME"]
    # data["time"] = "2016"
    # return 'The initnode json page'
    # Output: {u'age': 23, u'name': u'Peng Shuang', u'location': u'China'}
    # print data
    print(user,id,pw,name)
    return jsonify(data)











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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()





if __name__ == '__main__':
    #app.run()
    app.debug = True
    app.run(host='0.0.0.0')

