import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import sys
import bs4
import json
from bs4 import BeautifulSoup

"""res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElement = soup.select('.r a')
linkToOpen = min(5, len(linkElement))
for i in range(linkToOpen):
    webbrowser.open('https://google.com'+linkElement[i].get('href'))
"""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("good Evening")
    speak("I am Jarvis Sir. Please tell me how may I help you")
def news():
	print('Getting news...!')						#to get top 5 news from Google News
	q=requests.get('https://news.google.co.in/')
	soup=BeautifulSoup(q.text , "html.parser")
	l=[i.text for i in soup.findAll("span","titletext")]
	for i in range(5):
		print(l[i])
		speak(l[i])
		time.sleep(.2)
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@.com', 'yourpassword')
    server.sendmail('youremail@.com', to, content)
    server.close()

if __name__== "__main__":
    speak("Jarvis at your command Sir")
    wishMe()
    while True:
    #if 1:
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'read news' in query:
            news()


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open aws' in query:
            webbrowser.open("")
        elif 'hello jarvis' in query:
            speak('hello Sir')

        elif 'search'  in query:        
            speak('What should I search')
            content= takeCommand()
            print(content)
            webbrowser.open('https://google.com/search?q='+''.join(content))

        elif  'play music' in query:
            speak("sure sir")
            music_dir= 'F:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Rohan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'thank you' in query:
            speak("you welcome sir, What else I can do ")
        elif 'how are you' in query:
            speak("I am good sir. What about you?")
        elif 'me too' in query:
            speak("nice, so tell me sir what can I do for you")
        elif 'anything' in query:
            speak('Ahhhh please tell me clearly sir')
        elif 'email to rohan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Sender@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir  I am not able to send this email") 

     