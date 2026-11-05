import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pyaudio
import os
import subprocess
import pygame
import setuptools


# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = ""

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="<>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open study stark" in c.lower():
        webbrowser.open("https://study-stark.com")

    elif "open shorts" in c.lower():
        webbrowser.open("https://youtube.com/shorts")

    elif "power off" in c.lower():
        speak("Shutting down...")
        exit()

    elif "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com") 

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")

    elif "open gemini" in c.lower():
        webbrowser.open("https://gemini.com")

    elif "open replit" in c.lower():
        webbrowser.open("https://replit.com") 

    elif "chatgpt" in c.lower():
        webbrowser.open("https://chat.openai.com")

    elif "open vscode" in c.lower():
        webbrowser.open("vscode://")

    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")

    elif "open jio hotstar" in c.lower():
        webbrowser.open("https://hotstar.com")

    elif "open prime video" in c.lower():
        webbrowser.open("https://primevideo.com")

    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")

    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")

    elif "open perplexity" in c.lower():
        webbrowser.open("https://perplexity.com")

    elif "open grok" in c.lower():
        webbrowser.open("https://grok.com")

    elif "open copilot" in c.lower():
        webbrowser.open("https://copilot.com")

    elif "shutdown laptop" in c.lower():
        os.system("shutdown /s /t 5")

    elif "restart laptop" in c.lower():
        os.system("shutdown /r /t 5")

    elif "open notepad" in c.lower():
        subprocess.Popen("notepad.exe")

    elif "open calculator" in c.lower():
        subprocess.Popen("calc.exe")

    elif "open paint" in c.lower():
        subprocess.Popen("mspaint.exe")

    elif "open command prompt" in c.lower():
        subprocess.Popen("cmd.exe")

    elif "open vscode" in c.lower():
        subprocess.Popen("Code.exe")

    elif "open chrome" in c.lower():
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    elif "open edge" in c.lower():
        subprocess.Popen("msedge.exe")

    elif "open word" in c.lower():
        subprocess.Popen("winword.exe")

    elif "open excel" in c.lower():
        subprocess.Popen("excel.exe")

    elif "open powerpoint" in c.lower():
        subprocess.Popen("powerpnt.exe")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif c.lower().startswith("open "):
        app_name = c.lower().replace("open ", "")

        try:
            subprocess.Popen(app_name)
            speak(f"Opening {app_name}")
        except Exception:
            speak("Application not found")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    




if __name__ == "__main__":
    speak("Initializing Ultron....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "Ultron"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Assistant Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
