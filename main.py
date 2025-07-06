import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import json
from gtts import gTTS
import pygame
import os



engine = pyttsx3.init()
recognizer = sr.Recognizer()
newsapi = "a0bc6cd0d3554632b91cb8fd620145e6"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
        tts = gTTS(text)
        tts.save('temp.mp3')

        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the MP3 file
        pygame.mixer.music.load('temp.mp3')  # Replace with your actual file path

        # Play the music
        pygame.mixer.music.play()

        # Keep the program running until the music finishes
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove("temp.mp3")

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open hotstar" in c:
        webbrowser.open("https://www.hotstar.com/in/home")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c or "headlines" in c or "tell me news" in c: 
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=a0bc6cd0d3554632b91cb8fd620145e6")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news right now.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yaa")
                
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except Exception as e:
            print("Unexpected error: {0}".format(e))
