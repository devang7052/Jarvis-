import pyttsx3
from modules import sound as s
import speech_recognition as sr
import os
import pandas as pd
import webbrowser as web
import undetected_chromedriver as uc
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def search(file):
    data=pd.read_excel('apps.xlsx')
    b=len(data.index)
    for i in range(b):
        if data.loc[i,'apps']==file:
            return i
        
    speak('sorry i cant open this folder')
    return 'no'


def take_command(c):

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listning.........')
        if c==1:
            r.pause_threshold=0.5
            r.energy_threshold=1000
        else:
            r.pause_threshold=1
            r.energy_threshold=400
        audio=r.listen(source)
        print('ok')
    
    try:
        print('recognizing.....')
        query1=r.recognize_google(audio,language='en-in')
        query=query1.lower()
        print(f'user said: {query}')
        return query
    
    except Exception as e:
        print("please say that again")
        return 'none'
    
def openfile(a):
     data1=pd.read_excel('apps.xlsx')
     c=a.replace('open','')
     c=c.strip()
     row=search(c)
     if row=='no':
        None

     elif data1.loc[row,'mode']=='offline':
        os.chdir(data1.loc[row,'location'])
        os.startfile(data1.loc[row,'app name'])
        speak("anything else")
        
     else :
         url=data1.loc[row,'location']
         profile=data1.loc[row,'profile']
         options = uc.ChromeOptions()
         options.add_argument(f"--profile-directory=Profile {profile}")
         options.add_argument("user-data-dir=C:\\Users\\asus\\AppData\\Local\\Google\\Chrome\\User Data")
         driver =uc.Chrome(options=options,use_subprocess=True)
         driver.get(url)
         speak("anything else")




def download_song(b):
    d= s.download_sound(b)
    print(d)
    speak(d)
    speak("anything else")

def start_song(song_name):
    s.managesong(song_name)
    speak("anything else")
               
if __name__  == "__main__":
    while True:
        z=take_command(1)
        # z='jarvis'
        if z=='jarvis':  
            speak("hello sir")
            while True:             
                a=take_command(0)
                if 'download' in a:
                    song_name1=a.replace('download','')
                    download_song(song_name1.strip())

                if 'open' in a:
                   openfile(a)

                if a=='no thanks':
                    speak('ok, call me whenever you want, thanks')
                    z='none'
                    break

                if 'play ' in a:
                    song=a.replace('play','')
                    speak(f'playing {song.strip()}')
                    start_song(song.strip())
                   
                



