# program to server

import socket

listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222
listenerSocket.bind((serverIP,serverPort))
listenerSocket.listen(0)
print ('server siap menerima client')
while True:
    handlerSocket, addr = listenerSocket.accept()
    print ('sebuah client baru terkoneksi dengan alamat : ',addr)
    while True:
        message = input("Masukan pesan anda = ")
        str(handlerSocket.send(message))
        massage = handlerSocket.recv(1024)
        print ('pesan dari client : ',message)
        pass
    pass