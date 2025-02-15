from newsapi import base_news
import pyttsx3

# Initialize the news API client
newsapi = api_key="bd3cd9d551474e0aba8b971b309a7954"

# Initialize the TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 250)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    try:
        top_headlines = newsapi.get_top_headlines(language='en', country='us')
        articles = top_headlines['articles']
        if articles:
            speak("Here are the top headlines:")
            for i, article in enumerate(articles[:5]):  # Read out the top 5 news headlines
                speak(f"Headline {i + 1}: {article['title']}")
        else:
            speak("Sorry, I couldn't fetch the news right now.")
    except Exception as e:
        speak("An error occurred while fetching the news.")
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    latestnews()





