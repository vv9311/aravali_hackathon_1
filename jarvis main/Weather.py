import requests
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 250)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_weather(city):
    api_key = "52fd71b815d1c6b96e80ed982601dfe0"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["cod"]
        weather_desc = data["openweathermap"][0]["description"]
        temp = main["temp"] - 273.15  # Convert from Kelvin to Celsius
        speak(f"The temperature in {city} is {temp:.2f} degrees Celsius with {weather_desc}.")
    else:
        speak(f"City {city} not found.")
