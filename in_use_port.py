import socket
import timeit


def isUse(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)#shutdown参数表示后续可否读写
        print ('%d is ok' % port)
        return True
    # except Exception, e:
    except Exception as e:
        print(e)
        return False


def findPort():
    for i in range(1, 65535):
        if isUse('127.0.0.1', i):
            print (i)
#findPort遍历1-65535返回已占用端口。

if __name__ == '__main__':
    print (timeit.timeit("findPort()", 'from __main__ import findPort', number=1))
    #timeit模块提供计时功能，number为运行多少次数取平均值
#https://blog.51cto.com/tenderrain/1588739