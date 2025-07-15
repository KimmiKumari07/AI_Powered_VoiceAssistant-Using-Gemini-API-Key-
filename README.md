# 🧠 Jenny – Voice Assistant using Google Gemini API

Jenny is an AI-powered voice assistant written in **Python** that uses the **Google Gemini API** to understand and respond to natural language voice commands. It can search the internet, play music from YouTube, answer questions, and more—just like a smart personal AI!

---

## 📌 Features

- 🔊 **Text-to-Speech** (using `pyttsx3`)
- 🎙️ **Speech Recognition** for voice commands
- 🧠 **Natural Language Understanding** using **Google Gemini API**
- 🎵 **YouTube Music Playback** (via `pywhatkit`)
- 🌐 **Google Search Support**
- 🛑 **Exit Command Detection** (e.g., "Goodbye Jenny")

---

## 🚀 How It Works

1. The assistant captures your voice using a microphone.
2. Converts your speech into text using `speech_recognition`.
3. Sends the text to **Gemini** via the API to process and understand.
4. Responds intelligently via voice (`pyttsx3`).
5. Can perform actions like searching Google, playing music, or answering questions.

---

## 🛠️ Setup Instructions

### 
1. Install Requirements
```bash
pip install -r requirements.txt
```
2. Add Your Gemini API Key
In config.py
```bash
GEMINI_API_KEY = "YOUR_API_KEY"
```
With your actual API key from Google AI Studio.

---

▶️ Run the Assistant
```bash
python main.py
```
Say something like:

“Play a song”

“What is the capital of India?”

“Search for space facts”

“Goodbye Jenny” → will exit the assistant

📦 Dependencies
pyttsx3 – for offline text-to-speech

speechrecognition – for capturing and converting voice

pywhatkit – to play YouTube music

google-generativeai – Gemini API integration

You can find them listed in requirements.txt.

✨ Future Improvements
Add GUI with Tkinter or PyQt

Integration with home automation tools

Multilingual support
