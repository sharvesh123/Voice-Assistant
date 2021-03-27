import smtplib
import speech_recognition as sr
import pyttsx3
import cv2
import wikipedia
import datetime
import socket
import os
import webbrowser
import pyjokes
import requests
from bs4 import BeautifulSoup
import pywhatkit

# voice
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# speaking
def talk(word):
    engine.say(word)
    engine.runAndWait()


# microphone
def take_comand():
    try:
        with sr.Microphone() as source:
            print('listening sir...')
            talk('Listening sir')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command


def email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('', '')
    print('Tell me the email sir')
    talk('Tell me email the email id sir')
    emailname = input('Email:')
    print('tell me the content sir')
    talk('tell me the content sir')
    content = take_comand()
    server.sendmail('sharveshsantha974@gmail.com',
                    emailname,
                    msg=content
                    )
    print('Email has been sent')
# weather condition
def weather():
    res = requests.get('https://www.foreca.com/101270265/Har%C5%ABr-India')
    type(res)
    bs = BeautifulSoup(res.text, 'lxml')
    type(bs)
    weather2 = bs.find('div',attrs='w1dkr9i1')
    hi = bs.select('span')
    print(weather2.text)
    talk(weather2.text)
    print(hi[1].getText() + 'C')
    talk('temperature is'+hi[1].getText() + 'celsius')

def camera():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame1 = cam.read()
        if cv2.waitKey(10) == ord('q'):
             break
        cv2.imshow('Camera', frame1)

def whatsApp():
    print('tell the number sir')
    talk('tell me the number sir')
    number = take_comand()
    print('tell me the content sir')
    talk('tell me the content sir')
    content = take_comand()
    print('tell me the time sir')
    talk('tell me the time sir')
    timeH = int(take_comand())
    timeM = int(take_comand())
    pywhatkit.sendwhatmsg('+91'+number,content, timeH, timeM)




def run_assistant():
    command = take_comand()
    # playing music
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        print('playing musics sir...')
        talk('playing' + song + 'sir')
        # time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    # search
    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    # internet checking
    elif 'internet connectivity' in command or 'internet connection' in command:
        internet = command.replace('internet connectivity', '')
        ip = socket.gethostbyname(socket.gethostname())
        if ip == '127.0.0.1':
            print('No internet connectivity')
            talk('No internet connectivity')
        else:
            print('You are having internet connectivity enjoy')
            talk('You are having internet connectivity enjoy')
    # opening chrome
    elif 'open chrome' in command:
        url = 'www.google.com'
        webbrowser.open_new_tab(url)
        print('Opening chrome')
        talk('Opening chrome')
    # telling joke
    elif 'joke' in command or 'jokes' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    # asking how are you
    elif 'how are you' in command:
        print('I am fine. Whats about you?')
        talk('I am fine What about you')
        # asking who created you
    elif 'who created you' in command or 'are you from' in command:
        print('I were created by a intellingent person named sharvesh the programmer sir...')
        talk('I were created by intellingent person named sharvesh the programmer sir...')
    # opening android studio
    elif 'android studio' in command:
        os.startfile('')#you can enter your path
        talk('opening android studio')
    # open youtube
    elif 'youtube' in command:
        url2 = 'www.youtube.com'
        webbrowser.open_new_tab(url2)
        print('Opening youtube sir...')
        talk('opening youtube sir')
    # python
    elif 'in which programming language do you created by' in command:
        print('I have created fully in python sir...')
        talk('I have created fully in python sir')
    # opening vs code
    elif 'vs code' in command:
        vs = ''#vs code path
        os.startfile(vs)
        print('Open vs code sir...')
        talk('Opening vs code sir')
    # appriciate
    elif 'super' in command or 'good' in command:
        print('Thank you sir its my pleasure...')
        talk('Thank you sir its my pleasure')
    # joke
    elif 'speaking so much' in command:
        print('what do sir I have programmed like that...')
        talk('what do sir I have programmed like that')
        # opening google drive
    elif 'google drive' in command:
        drive_url = 'https://drive.google.com/drive/my-drive'
        webbrowser.open_new_tab(drive_url)
        print('opening google drive...')
        talk('opening google drive')
        # sending whatsapp
    elif 'whatsapp' in command:
        whatsApp()
    # hey there
    elif 'hey there' in command:
        print('I am here to serve you sir...')
        talk('I am here to serve you sir')
    # hi
    elif 'hai' in command:
        print('hi how can i help you sir...')
        talk('hi how can i help you sir')
        # weather
    elif 'weather' in command:
        weather()
    # exiting program
    elif 'stop' in command or 'exit' in command:
        talk('exited sir')
        exit()
    elif 'i am sorry' in command:
        talk('please dont ask sorry sir i am here to serve you')
    elif 'camera' in command:
        print('opening camera sir...')
        talk('opening camera sir')
        camera()
        talk('Your looking smart sir')

    elif 'thank you' in command:
        print('Yes sir')
        talk('yes sir')
    elif 'email' in command:
        email()

    elif 'did you have any feelings' in  command or 'you have feelings' in command or 'you have any feelings' in command:
        print('No sir I don\'t have any feelings')
        talk('No sir I don\'t have any feelings')

    elif 'open cmd' in command:
        print('opening cmd...')
        talk('opening cmd')
        os.startfile('C:\\Windows\\system32\\cmd.exe')

    elif 'i want to take screenshot' in command or 'snipping tool' in command:
        print('opening snipping tool')
        talk('opening snipping tool')
        os.startfile('C:\\Windows\\system32\\SnippingTool.exe')

    elif 'your age' in command:
        print('Old enough to know not to judge a book by its cover')
        talk('Old enough to know not to judge a book by its cover')

    elif 'your birthday' in command:
        print('well, birthdays mark the beginning of something,'
              'may be we can celebrate the day we met us '
              )
        talk('well, birthdays mark the beginning of something may be we can celebrate the day we met us ')

    else:
        talk('May be you are saying wrong or some features will be enabled in features')
   # running the program
while True:
    run_assistant()
