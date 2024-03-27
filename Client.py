import socket
import threading

HOST = "127.0.0.1"
PORT = 65321

clients = []
usernames = []

userName = input("what is your userName: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receiveChat():
    while True:
        try:
            message = client.recv(1024).decode()

            if(message == "@user"):
                client.send(userName.encode())
            
            else:
                print(message)
        
        except:
            print("")
            client.close()
            break

def writeMessage():
    while True:
        messague = input(f"")
        client.send(messague.encode())
        if(messague == "exit"):
            client.close()
            break
receiveMessage = threading.Thread(target=receiveChat)
receiveMessage.start()

writeM = threading.Thread(target=writeMessage)
writeM.start()
