import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said : {query}\n")
    except Exception as e:
        print("Say that Again pls")
        return "None"
    return query



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        