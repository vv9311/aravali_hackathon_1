import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

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
            elif "stop" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I can't do that yet.")
        else:
            wake_up_call()  # Return to wake-up call if the command is not recognized

if __name__ == "__main__":
    main()
