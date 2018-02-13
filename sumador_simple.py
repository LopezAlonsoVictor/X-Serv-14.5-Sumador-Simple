#!/usr/bin/python3

#Víctor López Alonso

import socket
import random
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 4000))
mySocket.listen(3)

try:
    while True:
        aux = random.randint(1,999999999)
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        request = str(recvSocket.recv(1024), 'utf-8')
        resource = request.split()[1]
        _,op1,operacion,op2 = resource.split('/')
        print(resource)
# respuesta
        html_answer = op1 + " " + operacion + " " + op2 + " = " + str(calculadora.funciones[operacion](int(op1),int(op2)))
        print(html_answer)
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n"+html_answer+"\r\n",'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
