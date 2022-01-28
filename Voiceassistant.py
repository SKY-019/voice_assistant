from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import speech_recognition as sr
from gtts import gTTS
import os, signal
from datetime import date
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import sys

# Google Calender (seangaming3690@gmail.com)
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()



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
    elif "stop program" in text:
        print("Closing Program")
        speak("Closing Program")
        os._exit(0) 