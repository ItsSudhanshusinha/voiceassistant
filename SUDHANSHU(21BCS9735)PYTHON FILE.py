import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("i am voice assistant sir. MADE BY SUDHANSHU SINHA. UID 21BCS9735. please tell me how may i help you")

def takecommand():
    #it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.....")
        r.pause_threshold = 2 # seconds of of non-speaking audio before a phrase is complete
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        speak("wait it is Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        speak("can you Say that again please....")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    while True:
       query = takecommand().lower()

       if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia","")
           result = wikipedia.summary(query,sentences=2)
           speak("According To Wikipedia")
           print(result)
           speak(result)

       if 'who' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia","")
           result = wikipedia.summary(query,sentences=2)
           speak("According To Wikipedia")
           print(result)
           speak(result)

       if 'what' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia","")
           result = wikipedia.summary(query,sentences=2)
           speak("According To Wikipedia")
           print(result)
           speak(result)

       if 'where' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia","")
           result = wikipedia.summary(query,sentences=2)
           speak("According To Wikipedia")
           print(result)
           speak(result)

       elif 'open youtube' in query:
            webbrowser.open("youtube.com")

       elif 'open google' in query:
            webbrowser.open("google.com")

       elif 'open facebook' in query:
            webbrowser.open("facebook.com")

       elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
       elif 'open play store' in query:
            webbrowser.open("play.google.com/store")

       elif 'play music' in query:
            music_dir = 'C:\\Users\\sudha\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%H:%S")
           speak(f"it is {strTime} sudhanshu")

       elif 'open code' in query:
           codePath = "C:\\Users\\sudha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)

       






    

 

