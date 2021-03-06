#!/usr/bin/env python
# coding=utf-8
'''
tcp服务器
它接受客户端发送的数据字符串
将其打上时间戳返回给客户端
'''
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        result = '[%s] %s' % (ctime(), data.decode('utf-8'))
        tcpCliSock.send(bytes(result, 'utf-8'))

    tcpCliSock.close()
tcpSerSock.close()
