import socket
import threading
from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

nickname = input("Enter your nickname: ")

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            encrypted_message = client.recv(1024)
            if not encrypted_message:
                break

            message = cipher.decrypt(encrypted_message).decode('utf-8')

            if message == "NICK":
                client.send(cipher.encrypt(nickname.encode('utf-8')))
            else:
                print(message)

        except:
            print("Disconnected from server!")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        encrypted_message = cipher.encrypt(message.encode('utf-8'))
        client.send(encrypted_message)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
