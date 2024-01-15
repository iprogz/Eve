import sqlite3
import subprocess
import speech_recognition as sr
from bard_ai import BardAI  # Importing BardAI class

# ... [Previous database functions] ...

# AI and command processing
r = sr.Recognizer()
bard_ai = BardAI()

def check_microphone_availability():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
        return True
    except OSError as e:
        print(f"Microphone error: {e}")
        print("Please ensure your microphone is connected and configured correctly.")
        return False

def parse_commands(user_input):
    # ... [Existing parsing logic] ...

def execute_command(command):
    # ... [Existing execution logic] ...

# Main application logic
def main():
    initialize_database()
    if not check_microphone_availability():
        return  # Exit if microphone is not available

    while True:
        try:
            print("Please say a command...")
            with sr.Microphone() as source:
                audio = r.listen(source)
                user_input = r.recognize_google(audio)
                print("You said:", user_input)

                # ... [Existing AI command processing logic] ...

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

