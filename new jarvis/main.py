# Enhanced Voice Assistant with Improved Speech Recognition
# Now allows more time to complete phrases and uses more reliable recognition.

import speech_recognition as sr
import os
import time
import webbrowser

###############################
# Command Configuration
###############################
COMMANDS_CONFIG = {
    "chrome": ("file", r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"),
    "discord": ("cmd", "start discord"),
    "youtube": ("url", "https://youtube.com"),
}

###############################
# Functions for Various Launch Types
###############################

def open_url(url: str):
    print(f"Opening website: {url}")
    webbrowser.open(url)


def open_file(filepath: str):
    if os.path.exists(filepath):
        print(f"Opening file: {filepath}")
        os.startfile(filepath)
    else:
        print(f"File not found: {filepath}")


def run_command(cmd: str):
    print(f"Executing command: {cmd}")
    os.system(cmd)


def open_generic_app(words_after_command: str):
    if words_after_command.strip():
        print(f"Attempting to launch: {words_after_command}")
        os.system(f'start "" "{words_after_command}"')
    else:
        print("Could not determine which application to open.")

###############################
# Command Handling Logic
###############################

def handle_open_command(user_text: str):
    user_text_lower = user_text.lower()
    for key, (launch_type, target) in COMMANDS_CONFIG.items():
        if key in user_text_lower:
            if launch_type == "url":
                open_url(target)
            elif launch_type == "file":
                open_file(target)
            elif launch_type == "cmd":
                run_command(target)
            return
    open_generic_app(user_text_lower)

###############################
# Improved Speech Recognition Function
###############################

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        print("Listening... Speak clearly and at a steady pace.")
        recognizer.adjust_for_ambient_noise(source, duration=1.5)
        audio = recognizer.listen(source, phrase_time_limit=10)

    response = {"success": True, "error": None, "transcription": None}
    try:
        response["transcription"] = recognizer.recognize_google(audio, language='en-US')
    except sr.RequestError:
        response["success"] = False
        response["error"] = "Recognition service error"
    except sr.UnknownValueError:
        response["error"] = "Could not understand the speech"
    return response

###############################
# Main Program Loop
###############################

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Voice Assistant started. Say 'Jarvis' followed by your command.")

    while True:
        result = recognize_speech_from_mic(recognizer, microphone)
        if not result["success"]:
            print(f"Error: {result['error']}")
            time.sleep(1)
            continue

        if result["transcription"]:
            user_text = result["transcription"].lower()
            print("You said:", user_text)

            if "jarvis" in user_text:
                handle_open_command(user_text)
        time.sleep(1)
