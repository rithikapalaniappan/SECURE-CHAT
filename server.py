import socket
import threading
from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

print("Server started. Waiting for connections...")

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def handle(client):
    while True:
        try:
            encrypted_message = client.recv(1024)
            if not encrypted_message:
                break

            message = cipher.decrypt(encrypted_message).decode('utf-8')
            print(message)

            encrypted_broadcast = cipher.encrypt(message.encode('utf-8'))
            broadcast(encrypted_broadcast)

        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                nicknames.remove(nickname)

                leave_message = f"{nickname} left the chat!"
                print(leave_message)
                broadcast(cipher.encrypt(leave_message.encode('utf-8')))
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send(cipher.encrypt("NICK".encode('utf-8')))
        nickname = cipher.decrypt(client.recv(1024)).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname: {nickname}")

        join_message = f"{nickname} joined the chat!"
        print(join_message)
        broadcast(cipher.encrypt(join_message.encode('utf-8')))

        client.send(cipher.encrypt("Connected to secure chat server!".encode('utf-8')))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
