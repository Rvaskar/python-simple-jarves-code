import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib 
import cv2
from gtts import gTTS
import pygame

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Rutik !")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon Rutik !")
        
    else:
        speak("Good Evening Rutik !")
        
    speak("im am Jarves Robo Sir. How may I help you?")



def takeCommand():
    #its take microphone command from the user and gives string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user Said: {query}\n ")

    except Exception as e:
        # print(e)
        print("Say that again..")
        return "none"

    return query

def search_web(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open_new_tab(url)
    
def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Captured Image", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("captured_image.jpg", frame)
        speak("Image captured and saved as captured_image.jpg.")
    else:
        speak("Sorry, unable to capture image.")

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com','your password')
#     server.sendmail('youremail@gmail.com',to,content)
#     server.close()

if __name__ == '__main__':
    speak("hello ")
    wishMe()
    
    while True:
        query = takeCommand().lower()
        #logic for executing task
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Acording to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Dell\\Desktop\\python project\\Robo\\music'              #exchange with your music location
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir. the time is {strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'  #exchange with your vs code location
            os.startfile(codePath)
            
        elif 'open camera' in query:
            # Capture image from camera
            capture_image()
            
        # elif 'send email to' in query:
        #     try:
        #         speak("what should i say?")
        #         content = takeCommand()
        #         to = "youremail@gmail.com"
        #         sendEmail(to,content)
        #         speak("Email has been send")
                
            # except Exception as e:
            #     print(e)
            #     speak("Sorry sir I am not able to send this mail")
            
        elif 'bye' in query:
                    speak("Goodbye, Sir!")
                    exit()
                    
        else:
            # Search the web using Chrome as the default browser
            search_web(query)