import pyttsx3
import datetime
import sys
import speech_recognition as sr
import wikipedia
import webbrowser as web
import pywhatkit
from pywikihow import search_wikihow
import pyautogui
import os
import keyboard
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import pyjokes
from PyDictionary import PyDictionary as Diction
from playsound import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    print("")
    engine.say(audio)
    print("")
    engine.runAndWait()


def wishMe():
     hour=int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         speak("Good Morning!")

   
   
     elif hour>=12 and hour<18:
         speak("Good Afternoon!")
    
    
     else:
        speak("Good Evening")

        
    
def takecommand():

    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio =r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")

        except Exception as e:
           # print(e)

            print("say that again please...")
            return "None"
        return query   
    

def takeHindi():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio =r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='hi')
            print(f"user said: {query}\n")

        except Exception as e:
           # print(e)

            print("say that again please...")
            return "None"
        return query       


def task_exe():
    speak("hellow sir , i am jarvis , i am online ")
    speak("how may i help you!")



def trans():
    speak("translator activated , speak sir!")
    line = takeHindi()
    translate = Translator()
    result1 = translate.translate(line)
    Text1 = result1.text
    speak(Text1)



def Music():
        speak("tell me the name of the song!")
        musicName = takecommand()
        
        pywhatkit.playonyt(musicName)
        speak("this is what i found sir, enjoy!")



def Whatsapp():

    speak("tell me the name of the person sir!")
    name = takecommand()

    if 'shobhit' in query:
        speak("tell me the message!")
        msg = takecommand()
        speak("tell me the time")
        speak("time in hour")
        hour = int(takecommand())
        speak("time in minutes")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+916392364689", msg, hour, min ,20)
        speak("sending message to master shikhar!")

    else:   
       speak("tell me the phone number!")
       phone = int(takecommand())
       ph = '+91' + phone
       speak("tell me the message sir!")
       msg = takecommand()
       speak("tell me the time")
       speak("time in hour")
       hour = int(takecommand())
       speak("time in minutes")
       min = int(takecommand())
       pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
       speak("sending message sir!")
       

def openApps(): 
    speak("ok sir,wait a second!")
    

    if ' chrome' in query:
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

    elif 'edge' in query:
        os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

    elif 'code' in query:
        os.startfile("C:\\Users\admin\Desktop\Microsoft VS Code\Code.exe")

    elif 'youtube' in query:
        web.open('https://www.youtube.com')   

    elif 'facebook' in query:
        web.open('https://www.facebook.com')

    elif' instagram' in query:
        os.startfile('https://www.instagram.com')   

    elif 'map' in query:
        web.open('https://www.google.com/maps/@27.141237,80.8833819,7z')

    elif 'portal' in query:
        web.open('https://erp.psitche.ac.in')    

    speak("opening sir")


def closeApps():
    speak("ok sir!")

    if 'youtube' in query:
        os.system("TASKKILL /F /im msedge.exe")

    elif'chrome' in query:
        os.system("TASKKILL /F /im chrome.exe")    

    elif'code' in query:
        os.system("TASKKILL /F /im code.exe")

    elif'maps' in query:
        os.system("TASKKILL /F /im msedge.exe")

    elif'instagram' in query:
        os.system("TASKKILL /F /im msedge.exe")    
        
    elif'facebook' in query:
        os.system("TASKKILL /F /im msedge.exe")    
    
    elif'edge' in query:
        os.system("TASKKILL /F /im msedge.exe")

    elif'portal' in query:
        os.system("TASKKILL /F /im msedge.exe")    
    
    speak("ok sir!")


def youtubeAuto():
    speak("whats your command sir")
    comm = takecommand()

    if 'pause' in comm:
        keyboard.press_and_release('sapcebar')

    elif'next video' in comm:
        keyboard.press_and_release('shif + n')

    elif'previous video' in comm:
            keyboard.press_and_release('shift + p')

    elif ' start' in comm:
        keyboard.press_and_release('k')

    elif'restart' in comm:
        keyboard.press_and_release('0')

    elif'mute' in comm:
        keyboard.press_and_release('m')

    elif'skip' in comm:
        keyboard.press_and_release('l')      

    elif'back' in comm:
        keyboard.press_and_release('j')

    elif'full screen' in comm:
        keyboard.press_and_release('f')

    elif'theatre mode' in comm:
        keyboard.press_and_release('t')

    speak("done sir")


def msedgeAuto():
    speak("say the command sir!")
    command = takecommand()

    if'close this tab' in command:
        keyboard.press_and-release('ctrl + w')

    elif'close this window' in command:
        keyboard.press_and_release('ctrl + shift + w')

    elif'open a new tab' in command:
        keyboard.press_and_release('ctrl + t')

    elif'open a new window' in command:
        keyboard.press_and_release('ctrl + n')

    elif'zoom in' in command:
        keyboard.press_and_release('ctrl + +')

    elif'zoom out' in command:
        keuboard.press_and_release('ctrl + -')                  
    
    speak("done sir!")


def Dict():
    speak("Dictionary Activated sir!")
    speak("tell me the word sir!")
    prob1 = takecommand()

    if 'meaning' in prob1:
        prob1 = prob1.replace("what is the ", "")
        prob1 = prob1.replace("jarvis", "")
        prob1 = prob1.replace("of", "")
        prob1 = prob1.replace("meaning of", "")
        result = Diction.meaning(prob1)
        speak(f"the meaning of {prob1} is {result}")

    elif 'synonym' in prob1:
        prob1 = prob1.replace("what is the ", "")
        prob1 = prob1.replace("jarvis", "")
        prob1 = prob1.replace("of", "")
        prob1 = prob1.replace("synonym of", "")
        result = Diction.synonym(prob1)
        speak(f"the synonym of {prob1} is {result}")

    elif 'antonym' in prob1:
        prob1 = prob1.replace("what is the ", "")
        prob1 = prob1.replace("jarvis", "")
        prob1 = prob1.replace("of", "")
        prob1 = prob1.replace("antonym of", "")
        result = Diction.antonym(prob1)
        speak(f"the antonym of {prob1} is {result}")

    speak("Exited Dictionary!")
    

def screenshot():
    speak("ok sir , what should i name that file ")
    path = takecommand()
    path1name = path + ".png"
    path1 = "E:\\shikhar\\screenshot1\\" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("E:\\shikhar\\screenshot1") 
    speak("here is your screenshot sir!")


def temp():
    search ="temperature in a kanpur"
    url = f"https://www.google.co.in/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ ="BNeawe").text
    speak(f"the temperature is {temperature}")


wishMe() 
task_exe()   
while True:


        query = takecommand().lower()

      
        if 'hello' in query:
         speak("hello sir , how are you")

        elif 'introduce yourself' in query:
            speak("hi i am jarvis i am an AI desktop assisstant program!")    
               
        elif 'I am good ' in query:
            speak("thats great sir")

        elif 'who is raghav' in query:
            speak("  raghav is master shikhar brother")
   
        elif 'wikipedia' in query:
         speak('searching wikipedia..')
         query = query.replace("wikipedia","")
         query = query.replace("jarvis", "")
         results = wikipedia.summary(query, sentences=2)
         speak(f"According to wikipedia : {results}")
         speak(results)

        elif 'youtube search' in query:
            speak("searching on youtube, this is what i found sir!")
            query =query.replace("jarvis", "")
            query =query.replace("youtube search", "")
            web3 = 'https://www.youtube.com/results?search_query=' + query
            web.open(web3)
            
        elif 'google search' in query:
         speak("this is what i found on google sir")
         query =query.replace("jarvis", "")
         query =query.replace("google search", "")  
         pywhatkit.search(query)
         speak(query)
         
        elif 'open hackerrank' in query:
          web.open("hackerrank.com")

        elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir the time is {strTime}")

        elif 'who is shobhit' in query:
            speak("master shobhit is master shikhar brother")

        elif 'website' in query:
            speak("opening website sir!") 
            query =query.replace("jarvis", "")
            query =query.replace("website", "")
            web1 =query.replace("open","")
            web2 ='https://www.' + web1 + '.com'
            web.open(web2)

        elif 'bye' in query:
            speak("ok sir,bye")    

        elif 'launch' in query:
            speak("tell me the name of the website sir!")
            name = takecommand()
            web.open(web2) 
            speak("done sir")   

        elif 'music' in query:
            Music()


        elif 'whatsapp message' in query:
            Whatsapp()   


        elif 'screenshot' in query:
           kk= pyautogui.screenshot()
           kk.save('D:\\screenshot')


        elif 'thank you' in query:
            speak("your welcome sir! ")

        elif 'open chrome' in query:
            openApps()


        elif ' open instagram' in query:
            openApps()


        elif 'open youtube' in query:
            openApps()

        elif 'open maps' in hquery:
            openApps()             
          
        elif ' open facebook' in query:
            openApps()             
              
        elif 'open code' in query:
            openApps()

        elif'open portal' in query:
            openApps()    

        elif ' close youtube' in query:
            closeApps()

        elif ' close maps' in query:
            closeApps()        

        elif ' close chrome' in query:
            closeApps()

        elif ' close facebook' in query:
            closeApps()

        elif ' close code' in query:
            closeApps()        

        elif ' close edge' in query:
            closeApps()

        elif ' close portal' in query:
            closeApps()       

        elif 'pause' in query: 
            keyboard.press_and_release('spacebar')

        elif 'start' in query:
             keyboard.press_and_release('k') 

        elif'next video' in query:
            keyboard.press_and_release('shif + n')

        elif'previous video' in query:
            keyboard.press_and_release('shift + p')

        elif 'restart' in query:
            keyboard.press_and_release('0')

        elif 'mute' in query:
            keyboard.press_and_release('m')

        elif 'skip' in query:
            keyboard.press_and_release('l')      

        elif 'back' in query:
              keyboard.press_and_release('j')

        elif 'full screen' in query:
              keyboard.press_and_release('f')

        elif 'theatre mode' in query:
            keyboard.press_and_release('t')

        elif 'youtube tools' in query:
            youtubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and-release('ctrl + w')

        elif 'close this window' in query:
            keyboard.press_and_release('ctrl + shift + w')

        elif 'open a new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open a new window' in query:
              keyboard.press_and_release('ctrl + n')

        elif 'zoom in' in query:
                keyboard.press_and_release('ctrl + +')

        elif 'zoom out' in query:
                 keyboard.press_and_release('ctrl + -') 

        elif 'msedge automation' in query:
            msedgeAuto()

        elif 'joke' in query:
            get = pyjokes.get_jokes()
            speak(get)

        elif 'repeat my command' in query:
            speak("ok sir, speak!")
            jj = takecommand()
            speak(f"you said : {jj}")


        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            speak("enter the time! ")
            time = input(": Enter the time :")

            while True:
                time_Ac = datetime.datetime.now()
                now = time_Ac.strftime("%H:%M:%S")

                if now==time:
                        speak("time to wake up sir!")
                        playsound('avengerstheme')
                        speak("alarm closed")

                elif now>time:
                    break        


        elif 'temperature' in query:
            temp()


        elif 'translator' in query:
            trans()


        elif ' how to' in query:
            speak("getting information from internet sir")
            op = query.replace("jarvis", "")
            max_result = 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        elif 'screenshot' in query:
            screenshot()


        elif ' taarif karo' in query:
         speak("tarif toh main kardunga phir nazar kaun utarega")


        elif 'you need a break' in query:
            speak("ok sir , you can call me anytime ")
            speak("just say wakeup jarvis")
            break
                               
        elif ' keep quiet' in query:
            speak("ok sir! ")
        
                 
                  
