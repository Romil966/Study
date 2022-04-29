import datetime
import os
import random
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(command):
    engine.setProperty('rate', 135)
    engine.say(command)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 7 <= hour <= 12:
        speak("Romil")
        speak("Good morning")
    elif 12 < hour <= 18:
        speak("Romil")
        speak("Good afternoon")
    else:
        speak("Romil")
        speak("Good evening")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning..")
        r.pause_threshold = 1
        r.energy_threshold = 150
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source)
        try:
            print("Analizning")
            text = r.recognize_google(audio, language='en-in')
            print(f"you said:{text}")
        except Exception as e:
            print("Sorry, Please say again")
            return "None"
    return text


if __name__ == "__main__":
    wishme()
    speak("I am Marvic")
    speak("I am ready to help you")
    while True:
        text = command().lower()

        if "wikipedia" in text:
            speak("Exploring wikipedia.....")
            text = text.replace("wikipedia", "")
            try:
                result = wikipedia.summary(text, sentences=3)
                speak("According to wikipedia...")
                print(result)
                speak(result)
            except Exception as e:
                print("Sorry, Please say again")

        elif "open youtube" in text:
            speak("Ok")
            speak("Openig youtube for you")
            webbrowser.open("youtube.com")

        elif "open google" in text:
            speak("Ok")
            speak("Opening google for you")
            webbrowser.open("google.com")

        elif "play music" in text:
            speak("ok")
            speak("Playing some song for you")
            path = r'E:\song'
            songs = os.listdir(path)
            num = random.randint(0, 2)
            os.startfile(os.path.join(path, songs[num]))

        elif "play song" in text:
            speak("ok")
            speak("Playing some song for you")
            path = r'E:\song'
            songs = os.listdir(path)
            num = random.randint(0, 2)
            os.startfile(os.path.join(path, songs[num]))

        elif "time please" in text:
            timeh = datetime.datetime.now().strftime("%H")
            timem = datetime.datetime.now().strftime("%M")
            print(timeh)
            speak("ok")
            speak(f"current time is {timeh} hour..{timem} minutes")
