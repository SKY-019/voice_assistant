import speech_recognition as sr
from gtts import gTTS
import os, signal
import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import sys

# Get Microphone
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, )
            print(said)
        except Exception as e:
            print("Exception " + str(e))
    return said

# Google Text to Speech
def speak(text):
    tts = gTTS(text=text, lang='en', tld='com')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    try:
        os.remove(filename)
    except OSError:
        pass

# Open Browser Tab
def openBrowser(url):
    webbrowser.open_new_tab(f"https://{url}")

# Open any URL
def openURL(url):
    speak(f"Openning{url}")
    openBrowser(url=url)

# Get Date
def getdate(text):
    text = text.lower()
    today = datetime.date.today()

while True:
    text = get_audio().lower()
    # Open Website
    if "open" in text:
        url=str(text).replace("open ", "")
        openURL(url=url)
    # Search Wikipedia
    elif "search" in text:
        speak("Searching Wikipedia")
        query = text.replace("search","")
        result = wikipedia.summary(query, sentences=1)
        speak("According to wikipedia")
        print(result)
        speak(result)
    # Close program
    elif "close program" and "stop program" in text:
        print("Closing Program")
        os._exit(0)
    elif "What date is it" in text:
        dateresult = datetime.datetime.now()
        print(today)
        speak(today) # NOT DONE