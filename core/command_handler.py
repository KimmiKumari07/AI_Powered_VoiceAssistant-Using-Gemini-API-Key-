import pywhatkit
from core.speaker import speak
from core.gemini import ask_gemini
import time
import sys

def handle_command(command):
    if not command:
        speak("I didn't catch that. Could you say it again?")
        return

    command = command.lower().strip()

    if "play" in command:
        song = command.replace("play", "").strip()
        if song:
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)
        else:
            speak("Please tell me what song you'd like to play.")

    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}.")
            pywhatkit.search(query)
        else:
            speak("Please specify what you'd like to search for.")

    elif any(exit_word in command for exit_word in ["goodbye", "exit", "stop", "shutdown"]):
        speak("Goodbye! Have a great day.")
        time.sleep(1.2)
        sys.exit()

    else:
        response = ask_gemini(command)
        if response:
            speak(response)
            time.sleep(0.4)  # Prevents voice engine overlap
        else:
            speak("I'm not sure how to respond to that. Try rephrasing.")