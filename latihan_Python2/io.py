import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-3].id)

engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""


def speak(audio):
    print('Arise Talk :' + audio)
    engine.say(audio)
    engine.runAndWait()

speak("Hello")
