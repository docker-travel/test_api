from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
import docker
import requests
import json
# client = docker.from_env()
# client = docker.DockerClient(base_url='tcp://106.104.114.80:2375')
client = docker.DockerClient(base_url='tcp://106.104.114.80:2375')


@app.route('/')
def index():
#     return 'Index Page'
	# return redirect(url_for('hello', username=request.form.get('username')))
	return redirect(url_for('static', filename='index.html'))

    # return render_template('black_cool_python3/index.html')

@app.route('/nodelist')
def nodelist():
    return 'The nodelist page'


@app.route('/containers/<string:port_id>')
def containers(port_id,):
    # show the post with the given id, the id is an integer
    # client = docker.DockerClient(base_url='tcp://106.104.114.80:'+port_id)
    r = requests.get('http://106.104.114.80:2375/containers/json')
    versionInfoPython = json.loads(r.text)
    # print ("Python 原始数据：", repr(r.text))
    # print ("JSON 对象：", versionInfoPython)
    print(versionInfoPython[0]['Id'])
    containers_list=list(map(lambda info: info['Id'], versionInfoPython))

    info=containers_list
    print(info)
    # containers_list=str.encode(client.containers.list())
    # containers_list=str(client.containers.list())
    # containers_list=versionInfoPython[0]['Id']
    print(client.containers.list())


    return '%s The containers page Post %s' %(info, port_id ) 




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

