import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine= pyttsx3.init('sapi5') 
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    else:
        speak("Good Evening!!!!!!!!!!!!!!")

    speak("MY name is David ")
    speak(" and I am developed by Aashish")
    speak("please tell me how may I help you")


def takeCommand():
   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n " )
     
    
    except Exception as e :
        print("Sorry...!! Say that again")
        speak("Sorry...!! Say that again")
        return "None"
    return query 



if __name__ =="__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open fb' in query:
            webbrowser.open("facebook.com")

        elif 'open fifa'in query:
            fifa_dir='D:\\Games\\FIFA 19'
            fifa= os.listdir(fifa_dir)
            os.startfile(os.path.join(fifa_dir, 'FIFA19'))

        elif 'open pycharm'in query:
            pycharm_dir='C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin'
            pycharm= os.listdir(pycharm_dir)
            os.startfile(os.path.join(pycharm_dir, 'pycharm64'))

        elif 'open vs code'in query:
            vscode_dir='C:\\Users\\Aashish\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(vscode_dir)

        elif 'exit' in query:
            speak("Thankyou")
            speak("will meet soon")
            wish = int(datetime.datetime.now().hour)
            if(wish>=4 and wish<16):
                speak(" and Have a good day")

            elif(wish>=16 and wish<21):
              speak(" and Have an enjoyable evening")
            
            else :
                speak(" and Good Night Sweet Dreams")
                
            break
            
        elif 'the time' in query:
            startTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {startTime}")
        
        elif 'who are you' in query:
            speak("I am David")

        elif 'hello' in query:
            speak("Hello")
            
        

        
        

            


    