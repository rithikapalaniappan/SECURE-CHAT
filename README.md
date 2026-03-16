# 🔐 Secure Chat Platform

A simple end-to-end encrypted chat application built in Python for secure messaging between users.

---

## 📌 Overview

Secure Chat Platform is a Python-based chat application that allows users to communicate securely using encryption.  
The project includes a **server**, a **client**, and a **key generation module** to support secure message exchange.

This project demonstrates the basics of:
- Secure client-server communication
- Message encryption and decryption
- Python socket programming
- Simple real-time chat system design

---

## ✨ Features

- 🔒 Encrypted chat messaging
- 💬 Real-time communication between client and server
- 🔑 Secret key generation using Python
- 🖥️ Separate client and server programs
- 📦 Lightweight and easy to run
- 🛠️ Beginner-friendly project structure

---

## 🏗️ Project Structure

```text
SECURE-CHAT/
├── client.py      # Client-side chat application
├── server.py      # Server-side chat application
├── key_gen.py     # Generates the secret key used for encryption
└── README.md      # Project documentation
## 🛠️ Technologies Used

- **Python**
- **Socket Programming**
- **Cryptography / Encryption**
- **Command Line Interface (CLI)**
Clone the repository
git clone https://github.com/rithikapalaniappan/SECURE-CHAT.git
cd SECURE-CHAT
Activate the virtual environment
Windows:
venv\Scripts\activate
▶️ How to Run
Step 1: Generate the secret key
python key_gen.py
Step 2: Start the server
python server.py
Step 3: Run the client
python client.py
🔐 Security Concept

This project uses a generated secret key to help secure communication between the client and server.
It is designed as a basic demonstration of encrypted messaging and secure communication concepts in Python.

🚀 Future Improvements

Add GUI for better user experience

Support multiple clients

Improve authentication system

Store chat history securely

Add stronger encryption workflow

👩‍💻 Author

Rithika Palaniappan
Engineering Student | Interested in Cybersecurity & Secure Systems

📄 License

This project is created for educational purposes.

