import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from Dictapp import openappweb, closeappweb  # Importing the Dictapp functions
from SearchNow import searchGoogle, searchYoutube, searchWikipedia  # Importing the SearchNow functions
from NewsRead import latestnews  # Importing the NewsRead function
from Weather import get_weather  # Importing the Weather function

# Initialize the TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 250)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 270
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def wake_up_call():
    while True:
        print("Waiting for wake-up call...")
        command = takecommand()
        if command and "wake up" in command.lower():
            speak("Yes, I am here. How can I assist you?")
            return

if __name__ == "__main__":
    wake_up_call()  # Ensure Jarvis waits for wake-up call first

    while True:
        query = takecommand().lower()
        if "go to sleep" in query:
            speak("Ok Sir, you can call me anytime")
            break
        elif "hello" in query:
            speak("Hello sir, how are you?")
        elif "i am fine" in query:
            speak("That's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("You are welcome, sir")
        elif "let's do some work jarvis" in query:
            speak("Yes sir, please tell me what can I do for you sir.")
        elif "i am tired" in query:
            speak("Playing your favourite songs, sir")
            a = (1, 2, 3)  # You can choose any number of songs (I have only chosen 3)
            b = random.choice(a)
            if b == 1:
                webbrowser.open("https://www.youtube.com/watch?v=jXwg9l9D51A")
        elif "pause" in query:
            pyautogui.press("k")
            speak("Video paused")
        elif "play" in query:
            pyautogui.press("k")
            speak("Video played")
        elif "mute" in query:
            pyautogui.press("m")
            speak("Video muted")
        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up, sir")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()
        elif "open" in query:
            openappweb(query)
        elif "close" in query:
            closeappweb(query)
        elif "google" in query:
            searchGoogle(query)
        elif "youtube" in query:
            searchYoutube(query)
        elif "wikipedia" in query:
            searchWikipedia(query)
        elif "news" in query:
            latestnews()
        elif "temperature" in query or "weather" in query:
            city = query.split("in")[-1].strip()  # Extract the city name
            get_weather(city)






