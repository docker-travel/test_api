import docker

# client = docker.from_env()
client = docker.DockerClient(base_url='tcp://106.104.114.80:2375')

# print(client.containers.list())

# print(client.images.list())
# print("==================")

# print(client.containers.list("status"))
# print("==================")
# print(client.containers.list("all"))

# print("==================")
# print(client.containers.list("since"))

# print("==================")
# print(client.containers.list("before"))
#client.login(username='sddivid',password='cs6owoqaq')
print("==================")
# print(client.containers.list(limit=-1,before='edcf9a4213',filters='status'))
# print(client.containers.list(before='edcf9a4213',filters=['status','name']))
# for container in client.containers.list(all=True, filters={"name":"star_with_"}):
#         print(container.name) 
for container in client.containers.list(all=True, filters={"status":"running"}):
        print(container.name)
print(client.containers.get('edcf9a4213').status)

print(client.containers.get('edcf9a4213').short_id)
print(client.containers.get('edcf9a4213').id)
print(client.containers.get('edcf9a4213').name)
print(client.containers.get('edcf9a4213').labels)
# print(client.containers.get('edcf9a4213').logs(timestamps=True))
print(client.containers.get('edcf9a4213').stop)
print(client.images.list())

print(client.containers.list())

image = client.images.pull('sddivid:cheers2019')

containerA = client.containers.run('cheers2019', 'echo hello world')
container = client.containers.run('latest', 'echo hello world')

print(containerA.logs())

# print(client.containers.list('edcf9a4213'))
# print(client.info())
# print(client.containers.list(all=True).edcf9a4213)
# print(client.containers.get('edcf9a4213').stats)
# print(client.containers.list('edcf9a4213').name)

# stats_obj=client.containers(quiet=False, all=False, trunc=False, latest=False, since=None, before=None, limit=-1, size=False, filters=None)
# print(stats_obj)

# for stat in stats_obj:
#         print(stat)
# AA=str(stats_obj)
# # def __repr__(self):
# #     return str(self.__dict__)

# print( client.version())





# cli = client(base_url='tcp://106.104.114.80:2375')
# len(cli.containers())
# # c.images(all)
# # c.images.list()