#!/usr/bin/env python
# coding=utf-8

from socket import *

HOST = '10.0.0.100'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    result = data.decode('utf-8')
    print(result)

tcpCliSock.close()
