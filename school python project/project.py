import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import socket
import os
import webbrowser
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(word):
    engine.say(word)
    engine.runAndWait()

def take_comand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace('assistant', '')
            print(command)
    except:
        print('something went wrong')
    return command

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Good morning sir')

    elif hour >= 12 and hour < 18:
        talk('Good afternoon sir')
    else:
        talk('Good evening sir')    





def run_assistant():
    command = take_comand()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)  
        talk('playing' + song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')      
        print(time)
        talk('Current time is'+time)
    elif 'search' in command:
        person = command.replace('search','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'internet connectivity' in command:
        internet = command.replace('internet connectivity','')
        ip = socket.gethostbyname(socket.gethostname())
        if ip == '127.0.0.1':
            print('No internet connectivity')
            talk('No internet connectivity')
        else:
            print('You are having internet connectivity enjoy')
            talk('You are having internet connectivity enjoy')
    elif 'open chrome' and 'open google' in command:
        chrome = command.replace('open chrome', '')
        url = 'www.google.com'
        webbrowser.open_new_tab(url)
        print('Opening chrome')
        talk('Opening chrome')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'how are you' in command:
        print('I am fine. Whats about you?')   
        talk('I am fine What about you') 
    
    elif 'how you created by' in command:
        talk('I were created by you')
 
    else:
        talk('May be you are saying wrong or some features will be enabled in features')    

wishme()
while True:
    run_assistant()  