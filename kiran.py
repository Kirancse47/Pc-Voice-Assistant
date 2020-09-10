import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
# print(voices[1].id)
engin.setProperty('voice',voices[0].id)


def speak(audio):
    engin.say(audio)
    engin.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good MOrning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good MOrning!")
    speak("I am kiran sir. Please tell me how may i help you")

def takeCommeand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:",query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content,j):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your emailId','email password')
    server.sendmail('your emailid',to,content)
    server.close()

if __name__ == "__main__":
    k=8391
    speak("Kiran is a good boy")
    wishMe()
    while True:
        query=takeCommeand().lower()
        # Logics for executing tasks....
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir='F:\\Musics\\ben'
            songs=os.listdir(music_dir)
            x=random.randint(0,37)
            print('Playing:',songs[x])
            speak("playing "+str(songs[x])+"  for you")
            os.startfile(os.path.join(music_dir,songs[x]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, now the time is {strTime}")
        
        elif 'open code' in query:
            codePath="C:\\Users\\KIRAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to suman' in query:
            try:
                speak("what should I say?")
                content=takeCommeand()
                to="receiver emailId"
                sendEmail(to,content,j)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir, I am unable to send email this time. please try again!")
            
        elif 'quit' in query:
            speak('thak you sir. have a good day...')
            break