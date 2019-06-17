from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
import docker
import requests
import json
from flask import jsonify
from flask import Response

import time,datetime

def create_docker_config(data):
    data={
                "USER_NAME": "fixiabis",
                "USER_EMAIL": "fixiabis@gmail.com",
                "NODE_USER_ID": "hash_id",
                "NODE_USER_PASSWORD": "password",
                "NODE_NAME": "node"
        }
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


print(create_docker_config({
  "USER_NAME": "fixiabis",
  "USER_EMAIL": "fixiabis@gmail.com",
  "NODE_USER_ID": "hash_id",
  "NODE_USER_PASSWORD": "password",
  "NODE_NAME": "node"
}))