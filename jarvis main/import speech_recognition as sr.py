import speech_recognition as sr
import pyttsx3
import requests
import datetime
import pygame
import webbrowser
from pytube import YouTube
import os
from transformers import pipeline

# Initialize the recognizer, TTS engine, and pygame mixer
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
pygame.mixer.init()

# Initialize the NLP model
nlp = pipeline("question-answering")

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None

def get_weather():
    api_key = "YOUR_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Ballabgarh"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        speak(f"The temperature is {temp - 273.15:.2f} degrees Celsius with {weather_desc}")
    else:
        speak("City not found!")

def play_music(file_path):
    if os.path.isfile(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        speak("Playing music")
    else:
        speak("Music file not found")

def stop_music():
    pygame.mixer.music.stop()
    speak("Music stopped")

def open_website(url):
    webbrowser.open(url)
    speak(f"Opening {url}")

def play_youtube_video(query):
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    speak(f"Searching YouTube for {query}")

def answer_question(question):
    context = "Your relevant context goes here."
    result = nlp(question=question, context=context)
    speak(result['answer'])

def wake_up_call():
    while True:
        print("Waiting for wake-up call...")
        command = listen()
        if command and "jarvis" in command.lower():
            speak("Yes, I am here. How can I assist you?")
            return

def main():
    speak("I am waiting for your command. Please say 'Jarvis' to activate me.")
    wake_up_call()
    while True:
        command = listen()
        if command:
            command = command.lower()
            if "hello" in command:
                speak("Hello! How are you?")
            elif "who are you" in command:
                speak("I am Jarvis, your personal assistant.")
            elif "weather" in command:
                get_weather()
            elif "time" in command:
                now = datetime.datetime.now().strftime("%H:%M")
                speak(f"The time is {now}")
            elif "play music" in command:
                play_music("path_to_music_file.mp3")  # Replace with the path to your music file
            elif "stop music" in command:
                stop_music()
            elif "open website" in command:
                open_website("https://www.example.com")  # Replace with your desired URL
            elif "play youtube" in command:
                query = command.replace("play youtube", "").strip()
                play_youtube_video(query)
            elif "answer" in command:
                question = command.replace("answer", "").strip()
                answer_question(question)
            elif "stop" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I can't do that yet.")
        else:
            wake_up_call()  # Return to wake-up call if the command is not recognized

if __name__ == "__main__":
    main()
