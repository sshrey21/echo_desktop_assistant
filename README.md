# 🤖 ECHO – AI-Powered Voice Assistant for Desktop Automation

**ECHO** is a Python-based voice-controlled AI assistant designed to streamline desktop interactions through natural language commands. Developed using **PyQt5**, this intelligent assistant enables seamless multitasking, accessibility support, and automation through voice-based interaction.

## 📌 Key Highlights

- ✅ **>90% voice recognition accuracy** in moderate-noise environments  
- ⚡ **<2 seconds** average response time for most commands  
- 🔊 Supports **15+ voice-activated operations** across different categories  
- 🧩 Modular and scalable design for easy expansion and integration

---

## ✨ Features

| Category        | Feature Description                                           |
|----------------|---------------------------------------------------------------|
| 🎙️ Voice Input   | Natural voice commands using SpeechRecognition               |
| 🔐 Authentication | Voice-based name + passcode system for secure access        |
| 💬 TTS Output    | Converts text responses to speech using pyttsx3              |
| ⚙️ System Control | Open apps, execute commands like shutdown, restart, etc.     |
| 🌐 Web Access     | Opens YouTube, searches Google, and fetches weather          |
| 📄 PDF Reader     | Reads PDF files aloud using speech output                    |
| 📷 Webcam         | Captures webcam photos using OpenCV                          |
| 🎵 Music Control  | Plays and pauses songs via voice commands                   |

---

## 🛠️ Tech Stack

- **Programming Language:** Python 3.11+
- **GUI Framework:** PyQt5
- **Voice Recognition:** `speech_recognition`
- **Text to Speech:** `pyttsx3`
- **PDF Handling:** `PyPDF2`
- **Webcam Access:** `opencv-python`
- **Other Libraries:** `requests`, `webbrowser`, `datetime`, `os`, `subprocess`

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/echo-desktop-assistant.git
cd echo-desktop-assistant
pip install -r requirements.txt
python main.py


