import docker

# client = docker.from_env()
client = docker.DockerClient(base_url='tcp://106.104.114.80:2375')
client.login(username='sddivid',password='cs6owoqaq')

##docker相关的方法使用
##使用DockerClient对象，会有以下方法：
print("==================")
client.api,
client.containers,
client.events,
client.from_env,
client.images,
client.info,
client.login,
client.networks,
client.nodes,
client.ping,
client.services,
client.swarm,
client.version,
client.volumes,
client.info()
print("==================")

print(client.images.list())
print(client.containers.list())
print(client.containers.get('edcf9a4213').name)
print("=========docker創建容器=========")

```
Command line:
$ docker run -itd -P --cpuset_cpus='0,1' --cpu_shares=2 --cpu_period=10000 --hostname=xxbandy --mem_limit=512m --net=none --oom_kill_disable=True -P -u admin busybox /bin/sh

Python API:
c1 = C.containers.run('busybox',command='/bin/sh',name='xxb-test',detach=True,tty=True,stdin_open=True,cpuset_cpus='0,1',cpu_shares=2,cpu_period=10000,hostname='xxbandy',mem_limit='512m',network_mode='none',oom_kill_disable=True,publish_all_ports=True,user='root')
run一个容器：类似于命令行的docker run方法
run(image, command=None, stdout=True, stderr=False, remove=False, **kwargs) method of docker.models.containers.ContainerCollection instance


func =client.containers.create(image, command=None, **kwargs) method of docker.models.containers.ContainerCollection instance

```
c1 = client.containers.run('busybox',command='/bin/sh',name='xxb-test',detach=True,tty=True,stdin_open=True,cpuset_cpus='0,1',cpu_shares=2,cpu_period=10000,hostname='xxbandy',mem_limit='512m',network_mode='none',oom_kill_disable=True,publish_all_ports=True,user='root')

print(client.containers.create)
c1.logs 
c1.name     # 获取容器名信息
c1.reload
c1.remove    #删除容器信息，相当于docker rm 参数：c1.remove(v=True,link=True,force=True)
c2.rename    #重命名容器名，相当于docker renmame oldname newname
c1.resize    #设置tty session信息
c1.restart   #重启容器信息
c1.start     #启动容器信息
c1.stats     #容器状态


print(client.images.list())


