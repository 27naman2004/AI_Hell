import speech_recognition as sr
import os

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Say the name of the application you want to open:")
    response = recognize_speech_from_mic(recognizer, microphone)

    if response["transcription"]:
        app_name = response["transcription"].lower()
        print(f"You said: {app_name}")

        if "notepad" in app_name:
            os.system("notepad.exe")
        elif "calculator" in app_name:
            os.system("calc.exe")
        else:
            print("Application not recognized or not supported.")
    else:
        print("I didn't catch that. What did you say?\n")

if __name__ == "__main__":
    main()