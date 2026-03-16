# 🔐 Secure Chat Platform

A production-grade end-to-end encrypted messaging platform built in Python.

## 📌 Overview

Secure Chat Platform is a Python-based messaging system designed with **end-to-end encryption**, **real-time communication**, and **security-first architecture**.  
It combines a **Flask REST API**, **asyncio WebSocket server**, and a **Tkinter desktop client** to deliver secure and efficient private messaging.

---

## ✨ Features

- 🔒 End-to-end encrypted messaging
- ⚡ Real-time communication using WebSockets
- 👤 User registration and login system
- 🛡️ Password hashing with bcrypt
- 📩 Send and fetch private messages
- ⏳ Self-destruct message TTL support
- 🚨 Intrusion detection and input sanitization
- 📜 Security, authentication, and audit logging
- 🚫 Sliding-window rate limiting
- 🔑 JWT-based token management
- 🖥️ Tkinter desktop client interface
- 🐳 Docker support for deployment
- 🌐 Nginx reverse proxy with TLS support

---

## 🏗️ Architecture

```text
secure_chat/
├── server/                    Flask REST API + asyncio WebSocket server
│   ├── app.py                 → Register, Login, Send, Fetch messages
│   ├── admin.py               → Admin Blueprint (ban/unban/promote/audit)
│   ├── auth.py                → bcrypt password hashing (rounds=12)
│   ├── database.py            → SQLite with WAL, indexes, sessions
│   ├── encryption.py          → Fernet/AES-128-CBC (key derived from SECRET_KEY)
│   ├── intrusion_detection.py
│   ├── logger.py              → security.log / auth.log / audit.log
│   ├── ratelimit.py           → Sliding-window rate limiter (thread-safe)
│   ├── sanitizer.py           → HTML escape, null-byte, length, SQL heuristic
│   └── websocket_server.py    → asyncio DM + broadcast
│
├── client/                    Tkinter GUI
│   ├── client_app.py          → Entry point
│   ├── login_window.py        → Dark-themed login screen
│   ├── register_window.py     → Register + live password strength meter
│   ├── chat_window.py         → Chat UI (dual WS+REST, self-destruct TTL)
│   ├── encryption_client.py   → Per-session Fernet cipher
│   └── websocket_client.py    → Non-blocking WS (asyncio in thread)
│
├── security/
│   ├── password_policy.py     → Strength regex + score breakdown
│   ├── hashing.py             → SHA-256 + HMAC-SHA-256 + timing-safe compare
│   ├── token_manager.py       → JWT HS256 (reads from config)
│   └── key_exchange.py        → X25519 identity key (future X3DH)
│
├── docker/
│   ├── Dockerfile.server
│   ├── Dockerfile.client
│   └── docker-compose.yml
│
├── nginx/
│   └── nginx.conf             → TLS 1.2/1.3, HSTS, WS upgrade, HTTP→HTTPS redirect
│
├── requirements.txt
├── start_server.bat           → Windows: auto-venv + launch Flask + WS
└── README.md
