import socket
import threading
from colorama import Fore, Back, Style 

HOST = "127.0.0.1"
PORT = 65321

clients = []
usernames = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

exitServer = False

def sendMessage(clientP, username, message = ""):
    for client in clients:
        if client != clientP:
            try:
                client.send(f"{username}: {message} ".encode())
            except:
                client.close()

def writeMessageUsers(client:socket.socket, _userName):
    while True:
        try:
            message = client.recv(1024).decode()
            sendMessage(client, _userName, message)
            print(f"{_userName} envio este mensajes...")
            print(Fore.LIGHTGREEN_EX + message + Style.RESET_ALL)
            print(type(message))
        except:
            sendMessage(clientP=client, username=_userName, message=f"system: the user:{_userName} disconnected")

def connetUsers():
    while True:
        client, address = server.accept()
        clients.append(client)

        client.send("@user".encode())
        userName = client.recv(1024).decode()
        usernames.append(userName)

        client.send("system: in joined to chat".encode())
        print(f"{userName} fue conectado en esta direccion {address}. \n ")
        sendMessage(client, userName, f"system: {userName} joined !!!")

        thread = threading.Thread(target=writeMessageUsers, args=(client,userName))
        thread.start()

connetUsers()