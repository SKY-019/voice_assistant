from __future__ import print_function # Google Calender (Needs to be at the very Top of code)

import datetime # Google Calender
import os.path # Google Calender
from google.auth.transport.requests import Request # Google Calender
from google.oauth2.credentials import Credentials # Google Calender
from google_auth_oauthlib.flow import InstalledAppFlow # Google Calender

from googleapiclient.discovery import build # Google Calender
from googleapiclient.errors import HttpError # Google Calender
import speech_recognition as sr # Getting Microphone
from gtts import gTTS # Google Text To speech
import os, signal # Functions for the operating system

from datetime import date # Time Function
import playsound # Play's audio file
import wikipedia # Searching for Wikipedia
import pyaudio # Play's also audio files
import webbrowser # Open Webbrowser Function

import sys # Standart ding
import pytz # Another Time Machine

# Google Calender (seangaming3690@gmail.com)
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def Calender_main():
    creds = None
    
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json",SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "W") as token:
            token.write(creds.to_jason())
    
    try:
        service = build("calender", "v3", Credentials=creds)
        time = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone("Europe/Berlin"))
        
        now = time.strftime("%B %A %d, %H:%M")
        print("Getting upcoming events")
        events_result = service.events().list(CalendarID="primary", timeMin=now, maxResults=10,
                                              singleEvents=True, orderBy="startTime").execute()
        events = events_result.get("items", [])
        
        if not events: 
            print("No upcoming events found.")
            return
        
        for event in events:
            start = event["start"].get("dateTime", event["event"].get("date"))