import pyttsx3

import speech_recognition as sr

import datetime

import wikipedia

import webbrowser

import os

import pyaudio

 

engine = pyttsx3.init('sapi5') #sapi5 for speech its a pyttsx3 engine

voices = engine.getProperty('voices')

#print(voices[0].id)

engine.setProperty('voice',voices[1].id)

 

 

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

 

 

def wishMe():

    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:

        speak('Good Morning')

    elif hour>=12 and hour<18:

        speak('Good Afternoon')

    else:

        speak('Good Evening')

    speak('I am iva. How may I assist you')

 

def takecommand():

    r= sr.Recognizer()

    with sr.Microphone() as source:

        print('Listening..............')

        r.pause_threshold=2

        audio=r.listen(source)

    try:

        print('Recognising............')

        query=r.recognize_google(audio,language='en-in')

        speak('you said ')

        speak(query)

 

        print(f'user said:{query}\n')

    except Exception as e:

        print(e)

 

        print('say that again please..')

        speak('say that again please')

        return 'none'

    return query 

 

 

 

if __name__=="__main__":

    wishMe()

    while True:

        query=takecommand().lower()

        #logic for operations

        if'wikipedia' in query:

            speak('searching wiki....')

            query=query.replace('wikipedia','')

            results=wikipedia.summary(query,sentences=2)

            speak('According to wikipedia')

            print(results)

            speak(results)

        elif 'who are u' in query:

            speak('I am your assistant. I can help you to search anything on wikipedia and opening many more stuffs')

        elif 'tell me about me' or 'what do you think of me' in query:

            speak('you are smart and you like having fun. i couldnot ask for a better boss')

        elif 'who developed you ' in query:

            speak('i was made by team virtual x')

        elif 'are you male or female' in query:

            speak('well, although my voice sounds female i am neither male nor female.')

        elif 'open youtube' in query:

            webbrowser.open('youtube.com')

 

        elif 'open oec website' in query:

            webbrowser.open('https://oec.ac.in/')

 

        elif 'open google' in query:

            webbrowser.open('google.com')

       

        elif 'open bput website' in query:

            webbrowser.open('http://www.bput.ac.in/')

   

 

        elif 'play music' in query:

            music_dir= 'D:\\mymusic\\songs'

            songs=os.listdir(music_dir)

            print(songs)

            os.startfile(os.path.join(music_dir,song[0]))