from core.listener import listen_command
from core.speaker import speak
from core.command_handler import handle_command
import time
import sys

WAKE_WORDS = ["hey jenny", "okay jenny"]
STOP_COMMANDS = ["goodbye", "bye", "stop", "shutdown", "exit"]

def wakeup_detected(text):
    return any(word in text.lower() for word in WAKE_WORDS)

def shutdown_detected(text):
    return any(word in text.lower() for word in STOP_COMMANDS)

speak("Jenny is now listening. Say 'Hey Jenny' to wake me up.")

while True:
    command = listen_command()
    if not command:
        continue

    if shutdown_detected(command):
        speak("Shutting down. Goodbye!")
        time.sleep(1.2)
        break

    if wakeup_detected(command):
        speak("Yes? I'm listening.")
        time.sleep(0.5)

        # Jenny stays awake in this loop
        while True:
            command = listen_command()
            if not command:
                speak("I didn't catch that. Could you repeat?")
                continue

            if shutdown_detected(command):
                speak("Shutting down. Goodbye!")
                time.sleep(1.5)
                sys.exit()

            if wakeup_detected(command):
                speak("Yes? I'm listening.")  # Restart the loop if wake word is heard again
                continue

            handle_command(command)
            time.sleep(0.5)