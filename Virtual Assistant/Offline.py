import speech_recognition as sr
import win32com.client
import webbrowser
import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.speak(text)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error processing your request.")
            return ""

if __name__ == "__main__":
    say("Hi, I am Jarvis, your A.I. Assistant. How can I assist you today?")
    print("Listening....")
    while True:
        query = takecommand()
        print(query)
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.org"],["google","https://www.google.com"]]
        for site in sites:
            if f"open {site[0]}" in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]}")
        if "open browser" in query.lower():
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            say("Opening Browser")
        if('good bye' in query.lower()):
            say("Bye. Meet you again soon.")
            break
        say(query)
