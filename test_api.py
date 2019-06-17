import requests
import json
import ast
r = requests.get('http://106.104.114.80:2375/containers/json')
# print(r.json())
print(r.status_code)
# my_str=r.text
# print (my_str['Id'])
#print (ast.literal_eval(my_str))

versionInfoPython = json.loads(r.text)
# print ("Python 原始数据：", repr(r.text))
# print ("JSON 对象：", versionInfoPython)

containers_list=list(map(lambda info: info['Id'], versionInfoPython))
print(containers_list)

# print(versionInfoPython[0])
# print(versionInfoPython[0]['Id'])


# print ("data2['name']: ", versionInfoPython['Id'])
# print ("data2['url']: ", versionInfoPython[0])