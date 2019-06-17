
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# from flask import Flask
import os
import sys
from flask import Flask
from flask import request
from flask import  jsonify

# from flask import request, jsonify, json, Module
# from web.utils.consts import POST, GET
# from web.db.dbSession import DBManager
# from web.db.models import Class

app = Flask(__name__)


@app.route('/')
def hello_world():
    os.system(" echo 'hello world!' ")
    # os.system("ls")

    return 'Hello World!'
@app.route('/mail', methods=['POST'])

def mail():
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
    # getForm = request.form.get()

    # print (getForm)
    print (content["COMPANY"])
    print (content["MESSAGE"])
    print (content["NAME"])
    print (content["MAIL"])
    os.system("echo "+"公司"+content["COMPANY"] +"訊息"+ content["MESSAGE"]+"名稱"+content["NAME"]+ " | ssmtp sddivid@gmail.com")

    print (content)
    return ('JSON posted')





# if __name__ == '__main__':
#     app.run()
if __name__ == "__main__" :
    app.run(host= '0.0.0.0' , port= 5001 )
# sudo mv /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default.conf.bak

# $ sudo rm /etc/nginx/sites-enabled/default


#echo "This is a test" | ssmtp recipient@your.domain.com