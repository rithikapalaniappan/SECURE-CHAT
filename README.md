# SECURE-CHAT
A production-grade end-to-end encrypted messaging platform built in Python.

Architecture
secure_chat/
├── server/             Flask REST API + asyncio WebSocket server
│   ├── app.py          → Register, Login, Send, Fetch messages
│   ├── admin.py        → Admin Blueprint (ban/unban/promote/audit)
│   ├── auth.py         → bcrypt password hashing (rounds=12)
│   ├── database.py     → SQLite with WAL, indexes, sessions
│   ├── encryption.py   → Fernet/AES-128-CBC (key derived from SECRET_KEY)
│   ├── intrusion_detection.py
│   ├── logger.py       → security.log / auth.log / audit.log
│   ├── ratelimit.py    → Sliding-window rate limiter (thread-safe)
│   ├── sanitizer.py    → HTML escape, null-byte, length, SQL heuristic
│   └── websocket_server.py → asyncio DM + broadcast
├── client/             Tkinter GUI
│   ├── client_app.py   → Entry point
│   ├── login_window.py → Dark-themed login screen
│   ├── register_window.py → Register + live password strength meter
│   ├── chat_window.py  → Chat UI (dual WS+REST, self-destruct TTL)
│   ├── encryption_client.py → Per-session Fernet cipher
│   └── websocket_client.py  → Non-blocking WS (asyncio in thread)
├── security/
│   ├── password_policy.py → Strength regex + score breakdown
│   ├── hashing.py         → SHA-256 + HMAC-SHA-256 + timing-safe compare
│   ├── token_manager.py   → JWT HS256 (reads from config)
│   └── key_exchange.py    → X25519 identity key (future X3DH)
├── docker/
│   ├── Dockerfile.server
│   ├── Dockerfile.client
│   └── docker-compose.yml
├── nginx/nginx.conf    → TLS 1.2/1.3, HSTS, WS upgrade, HTTP→HTTPS redirect
├── config.py           → All settings via environment variables
├── requirements.txt
├── start_server.bat    → Windows: auto-venv + launch Flask + WS
└── start_client.bat    → Windows: launch Tkinter client
Quick Start (Windows)
cd i:\secure\secure_chat

# Install dependencies
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Start both servers (two separate windows)
start_server.bat

# Start the client
start_client.bat
API Endpoints
Method	Route	Auth	Description
POST	/register	—	Create account
POST	/login	—	Get JWT token
POST	/send	Bearer JWT	Send encrypted message
GET	/messages	Bearer JWT	Fetch & decrypt messages
GET	/health	—	Health check
GET	/admin/users	Admin-Key	List all users
POST	/admin/ban/<user>	Admin-Key	Ban a user
POST	/admin/unban/<user>	Admin-Key	Unban a user
POST	/admin/promote/<user>	Admin-Key	Promote to admin
GET	/admin/messages	Admin-Key	List all messages
GET	/admin/security_events	Admin-Key	View security log
Security Features
Feature	Implementation
Password hashing	bcrypt (work factor 12)
JWT auth	HS256, 1-hour TTL, iat+exp claims
Symmetric encryption	Fernet (AES-128-CBC + HMAC-SHA256), key derived from SECRET_KEY
Message integrity	SHA-256 hash stored alongside ciphertext
Rate limiting	Sliding window, 30 req/min per user (thread-safe)
Input sanitization	HTML escape, null-byte detection, field length caps
SQL injection	Parameterised queries + heuristic logging
Self-destruct	Per-message TTL, background worker deletes expired messages
Brute-force protection	Incremental login attempt counter → alert at 5 failures
Admin audit trail	Every privileged action logged to audit.log
Intrusion detection	SQL injection, unauthorized access, brute force hooks
Future E2EE	X25519 identity key ready for X3DH / Double Ratchet
Docker Deployment
cd i:\secure\secure_chat
docker-compose -f docker/docker-compose.yml up -d
⚠️ Change all secrets in config.py (or via environment variables) before production use!

Environment Variables
Variable	Default	Description
SECRET_KEY	CHANGE_THIS_SECRET_IN_PRODUCTION	Fernet key derivation + Flask secret
ADMIN_KEY	ULTRA_SECRET_ADMIN_CHANGE_ME	Admin endpoint header
TOKEN_SECRET	TOKEN_SECRET_CHANGE_IN_PRODUCTION	JWT signing key
CHAT_DB	chat.db	SQLite database path
CHAT_HOST	0.0.0.0	Flask bind address
CHAT_PORT	5000	Flask port
WS_PORT	6789	WebSocket port
