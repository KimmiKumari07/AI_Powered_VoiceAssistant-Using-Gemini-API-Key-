import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)

# Optional: voice selection
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Try voices[1] on some systems

def clean_text(text):
    return text.replace("*", "").replace("•", "").replace("–", "-").strip()


def speak(text):
    final_text = clean_text(text)

    print("🤖 Jenny:", final_text, flush=True)
    try:
        engine.say(final_text)
        engine.runAndWait()
    except Exception as e:
        print("⚠️ Speak Error:", e)