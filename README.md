# 🔐 FileVault - Secure File Vault System

> A modern, production-ready secure file vault with React frontend, FastAPI backend, AES-256-GCM encryption, and mobile PWA support for Android & iOS

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![React](https://img.shields.io/badge/React-18%2B-blue)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)](https://fastapi.tiangolo.com)

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Security Design](#security-design)
- [Installation Guide](#installation-guide)
- [How It Works](#how-it-works)
- [Usage Guide](#usage-guide)
- [PWA Setup](#pwa-setup-android--ios)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)

---

## 🎯 About The Project

**FileVault** is a comprehensive cybersecurity engineering project demonstrating modern secure file storage architecture using client-side encryption, RESTful APIs, and progressive web app technology.

### Project Purpose
This project was built as an academic engineering demonstration showcasing:
- **Encryption-at-rest** using AES-256-GCM authenticated encryption
- **Password-based key derivation** with PBKDF2-HMAC-SHA256  
- **Modern web security** patterns and best practices
- **Cross-platform compatibility** (Desktop & Mobile via PWA)
- **Production-ready code structure** with proper separation of concerns

### Why FileVault?

In an era where data breaches and unauthorized access are common threats, FileVault provides:
- ✅ **Zero-knowledge architecture** - Files encrypted before upload
- ✅ **Client-side encryption** - Server never sees plaintext
- ✅ **Secure deletion** with cryptographic overwriting
- ✅ **Tamper detection** via authenticated encryption (GCM mode)
- ✅ **Mobile-first design** with PWA installability

---

## ✨ Features

### Core Security Features
- 🔒 **AES-256-GCM Encryption** - Industry-standard authenticated encryption
- 🔑 **PBKDF2 Key Derivation** - 100,000+ iterations with random salt per file
- 🛡️ **Tamper Detection** - Integrity verification on decryption
- 🗑️ **Secure Deletion** - Cryptographic shredding before file removal
- 📝 **Audit Logging** - Complete audit trail of all operations

### User Experience
- 🎨 **Modern Dark UI** - Clean, minimal interface with high contrast
- 📤 **Drag & Drop Upload** - Intuitive file upload experience
- 🔍 **Real-time Search** - Filter files instantly
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🖼️ **File Preview** - View images and text files securely
- 📊 **File Management** - Category tagging, notes, and metadata

### Mobile & PWA
- 📲 **Progressive Web App** - Install like a native app
- 🌐 **Offline Support** - Service worker caching
- 🏠 **Add to Home Screen** - Android & iOS compatible

---

## 🛠️ Technology Stack

### Frontend
- **React 18** - Modern UI library with hooks
- **Vite** - Lightning-fast build tool
- **CSS3** - Custom dark theme
- **Web Crypto API** - Browser-native encryption

### Backend
- **FastAPI** - High-performance Python web framework
- **Uvicorn** - ASGI server
- **Python Cryptography** - Secure encryption library
- **Pydantic** - Data validation

### Security
- **AES-256-GCM** - Authenticated encryption
- **PBKDF2-HMAC-SHA256** - Key derivation function
- **CORS** - Cross-origin resource sharing
- **Secure file handling** - Path sanitization

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────┐
│              USER DEVICE                        │
│  ┌──────────────────────────────────────────┐  │
│  │    React Frontend (PWA)                  │  │
│  │  • Drag & Drop UI                        │  │
│  │  • File Preview                          │  │
│  │  • Search & Filter                       │  │
│  └──────────────────────────────────────────┘  │
│                    ↕ HTTPS                      │
│  ┌──────────────────────────────────────────┐  │
│  │    FastAPI Backend                       │  │
│  │  • REST API Endpoints                    │  │
│  │  • File Upload/Download                  │  │
│  │  • Encryption Layer                      │  │
│  └──────────────────────────────────────────┘  │
│                    ↕                            │
│  ┌──────────────────────────────────────────┐  │
│  │    File System Storage                   │  │
│  │  • /storage/files/   (encrypted blobs)   │  │
│  │  • /storage/metadata/  (file index)      │  │
│  │  • /storage/audit/  (deletion logs)      │  │
│  └──────────────────────────────────────────┘  │
└────────────────────────────────────────────────┘
```

---

## 🔐 Security Design

### Encryption Workflow

1. **Key Derivation**
   ```
   User Password + Random Salt (16 bytes)
         ↓
   PBKDF2-HMAC-SHA256 (100,000 iterations)
         ↓
   256-bit Encryption Key
   ```

2. **File Encryption**
   ```
   Original File Bytes
         ↓
   AES-256-GCM Encryption (with random IV)
         ↓
   Encrypted Package: [Salt | IV | Ciphertext | Auth Tag]
   ```

3. **Storage**
   ```
   Server stores ONLY:
   - Encrypted binary blob (no plaintext)
   - Metadata (filename, size, category, timestamp)
   - Audit logs (action, timestamp, file ID)
   ```

### Security Properties

✅ **Confidentiality** - AES-256 encryption protects file content  
✅ **Integrity** - GCM mode provides authentication tag  
✅ **Authenticity** - Password verification via key derivation  
✅ **Forward Secrecy** - Unique salt per file  
✅ **Tamper Resistance** - Decryption fails if file is modified

### Threat Model

**Protected Against:**
- Unauthorized file access
- Data breach (encrypted storage)
- Man-in-the-middle attacks (HTTPS)
- File tampering (authenticated encryption)
- Weak passwords (PBKDF2 iterations)

**Not Protected Against:**
- Keyloggers on client device
- Compromised user password
- Physical access to unlocked device

---

## 📥 Installation Guide

### Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- **npm or yarn**
- **Git**

### Step 1: Clone Repository

```bash
git clone https://github.com/nahshalmeethal/filevault-secure-vault.git
cd filevault-secure-vault
```

### Step 2: Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create storage directories
mkdir -p storage/files storage/metadata storage/audit

# Run server
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Backend runs at: `http://127.0.0.1:8000`

### Step 3: Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Frontend runs at: `http://127.0.0.1:5173`

### Step 4: Verify Installation

1. Open `http://127.0.0.1:5173` in browser
2. You should see the FileVault dark dashboard
3. API docs at `http://127.0.0.1:8000/docs`

---

## ⚙️ How It Works

### 1. File Upload Process

```
User selects file → Frontend reads bytes → User enters password 
→ Derive key (PBKDF2) → Encrypt (AES-256-GCM) 
→ Send to backend → Save encrypted blob + metadata 
→ Return file ID
```

### 2. File Download/Decrypt

```
User requests file → Backend sends encrypted blob 
→ User enters password → Derive key → Verify auth tag 
→ Decrypt → Display/download plaintext
```

### 3. Secure Deletion

```
User deletes → Overwrite with random bytes → Delete file 
→ Log to audit → Remove metadata
```

---

## 📖 Usage Guide

### Adding Files

1. Click drag & drop zone or browse
2. Select any file type
3. Enter password (required)
4. Add label, category, notes (optional)
5. Click **Encrypt & Upload**

### Viewing Files

- Browse in dashboard list
- Search by name
- Preview images/text
- Download to decrypt

⚠️ **Important**: Forgotten passwords cannot be recovered

---

## 📱 PWA Setup (Android & iOS)

### Android (Chrome/Edge)

1. Deploy to HTTPS (Vercel/Netlify)
2. Visit URL on Chrome
3. Tap **Install** prompt
4. App appears on home screen

### iOS (Safari)

1. Deploy to HTTPS
2. Open in Safari
3. Tap Share → **Add to Home Screen**
4. App icon appears

### Deployment

**Frontend (Vercel):**
```bash
npm install -g vercel
cd frontend
npm run build
vercel --prod
```

**Backend (Railway/Render):**
- Push to GitHub
- Connect to hosting platform
- Deploy

---

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints

**Upload File**
```http
POST /api/files/upload
Content-Type: multipart/form-data

Parameters:
- file: File (required)
- password: string (required)
- label, category, notes: string (optional)
```

**List Files**
```http
GET /api/files
```

**Get File**
```http
GET /api/files/{file_id}
```

**Delete File**
```http
DELETE /api/files/{file_id}
```

### Interactive Docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 📁 Project Structure

```
filevault-secure-vault/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app
│   │   ├── core/config.py       # Config
│   │   ├── routes/files.py      # Endpoints
│   │   └── services/storage.py  # Encryption logic
│   ├── storage/                 # File storage
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx             # Main component
│   │   ├── main.jsx            # Entry point
│   │   └── styles/app.css      # Dark theme
│   ├── public/manifest.webmanifest
│   ├── package.json
│   └── vite.config.js
└── README.md
```

---

## 🚀 Future Enhancements

- [ ] User authentication (JWT)
- [ ] Database integration
- [ ] File sharing with password links
- [ ] Two-factor authentication
- [ ] File versioning
- [ ] Real-time sync
- [ ] Native mobile apps

---

## 📄 License

MIT License - see LICENSE file

---

## 👨‍💻 Author

**Nahshal Meethal**  
GitHub: [@nahshalmeethal](https://github.com/nahshalmeethal)

---

## ⚠️ Disclaimer

This is an educational demonstration. While it implements industry-standard encryption, it has not undergone professional security audits. For production use, conduct thorough security reviews.

---

**Built with ❤️ for Cybersecurity Education**
