import webbrowser
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def open_websites():
    websites = {
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "stackoverflow": "https://www.stackoverflow.com"
    }
    
    speak("Which website do you want to open?")
    command = listen()
    
    for key in websites:
        if key in command:
            webbrowser.open(websites[key])
            speak(f"Opening {key}")
            return
    
    speak("Sorry, I couldn't find the website you mentioned.")

if __name__ == "__main__":
    open_websites()

