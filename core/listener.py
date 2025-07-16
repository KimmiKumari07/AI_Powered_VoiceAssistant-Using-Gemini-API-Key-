import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            command = recognizer.recognize_google(audio)
            print("🗣️ You said:", command)
            return command
        except sr.WaitTimeoutError:
            print("⏳ Timeout: No speech detected.")
            return ""
        except sr.UnknownValueError:
            print("🤷 Couldn't understand.")
            return ""
        except sr.RequestError as e:
            print("❌ API Error:", e)
            return ""