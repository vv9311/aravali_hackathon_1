import os
import webbrowser

def openappweb(query):
    if "notepad" in query:
        os.startfile("notepad.exe")
    elif "calculator" in query:
        os.startfile("calc.exe")
    elif "browser" in query:
        webbrowser.open("https://www.google.com")
    elif "youtube" in query:
        webbrowser.open("https://www.youtube.com")
    else:
        print("Application or website not recognized.")

def closeappweb(query):
    if "notepad" in query:
        os.system("taskkill /f /im notepad.exe")
    elif "calculator" in query:
        os.system("taskkill /f /im calc.exe")
    else:
        print("Application not recognized.")
