import requests
from bs4 import BeautifulSoup
from googlesearch import search
import pandas as pd
import re
import os
import pyglet
import speech_recognition as sr
import webbrowser as web
from pytube import YouTube
from moviepy.editor import *
import threading
import pyautogui
import time
from fp.fp import FreeProxy
import pyttsx3
constant='no'

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hit_trial(a,soup,website,row):
    try:
        z=a.title()
        y=z.replace(' ','-')
        url_parent=soup.find(href=re.compile(y))
        url1=url_parent.get('href')
        return url1

    except:
        try:
            content_finder=soup.find(string=f'{a.title()}.mp3')
            main_link=content_finder.findParent('a')
            url1=main_link.get('href')
            return url1
                
        except:
            try:
                

                content_finder=soup.find(string=website.loc[row,'string'])
                main_link=content_finder.findParent('a')
                url1=main_link.get('href')
                return url1
            except:
                return 'sorry'
                

def download_by_youtube(query):
        
            query1=f'{query} song youtube'
            a=[]
            for i in search(query1,num=5,stop=5):
                if 'www.youtube.com' in i:
                    a.append(i)
                    break
                
            url=a[0]
            
            yt = YouTube(url)
            print(url)
            print('downloading...')
            stream = yt.streams.get_audio_only()
            stream.download(filename=f'songs/{query}.mp3')

            return 'song downloaded'
        
        

def download_sound(a):
    try:  
        if check(a):
            return1=download_by_youtube(a)
            return return1
        else:
            return 'song already downloaded'
    except:
        return2=download_sound_web(a)
        return return2
def download_sound_web(a):
    try:
        query=a
        query1=f'{query} song download'
        website= pd.read_excel('modules/websites.xlsx')
        t=0
        
        for i in search(query1,num=9,stop=9):
            
            b=len(website.index)
            for j in range(b):
                if  website.loc[j,'name'] in i:
                    url=i
                    row=j
                    t=1
                    break
        if(t!=1):        
            return 'sorry'
        print(url)

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        if website.loc[row,'type']=='class':
            class1= website.loc[row,'class']
            content_finder=soup.find('a',class_=class1)
            url1=content_finder.get('href')
        else:
            url1=hit_trial(a,soup,website,row)
        print(url1)
        link=website.loc[row,'link']
        f=requests.get(f'{link}{url1}')
        f1=open(f'songs/{query.lower()}.mp3','wb')        
        f1.write(f.content)
        f1.close()
        return 'song downloaded'
    except:
        return 'sorry'

def play_youtube_song(query):
    query1=f'{query} song youtube'
    a=[]
    for i in search(query1,num=5,stop=5):
        if 'www.youtube.com' in i:
                a.append(i)
                break

    url=a[0]
    print(url)
    chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe'
    web.register('chrome',None,web.BackgroundBrowser(chrome_path))
    web.get('chrome').open_new_tab(url)
    
        

def check(song):
    if os.path.exists(f'songs/{song}.mp3'):
        return False
    else:
        return True
  
def managesong(song_name,time_stamp=0):  
    global constant
    try:
        orignal=os.getcwd()
        os.chdir('songs')  
        list=os.listdir()
        search=f'{song_name}.mp3'
        if search in list:
        
            player = pyglet.media.Player()

            song = pyglet.media.load(search)
            
            if  constant=='close':
                print('o')
                pyautogui.hotkey('ctrl', 'w')
            
            player.queue(song)

            print(time_stamp)
            player.seek(time_stamp)
            player.play()
            
            os.chdir(orignal)
            while True:
                i=take_command()
                if i=='stop':
                    player.pause()
                elif i=='exit':
                    return None
                elif i=='play':
                    player.play()
            
            window = pyglet.window.Window()
            pyglet.app.run()
        else:
            os.chdir(orignal)
            # b=play_youtube_song(song_name)
            speak(f'downloading your sound please wait')
            time1=time.time()
            a=download_sound(song_name)
        
            if a=='song downloaded':

                # pyautogui.hotkey('ctrl', 'w')
                constant='close'
                time2=time.time()-time1    
                managesong(song_name,time2)
            else:
                while True:
                    i=take_command()
                    if i=='stop':
                        pyautogui.hotkey('ctrl', 'w')
                        break
    except:
        if os.path.exists(f'{song_name.lower()}.mp3'):
            os.remove(f'{song_name.lower()}.mp3')
        while True:
            i=take_command()
            if i=='stop':
                pyautogui.hotkey('ctrl', 'w')
                break
            
        
        

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listning.........')
        r.phrase_threshold=0.1
        r.pause_threshold=0.5
        r.energy_threshold=300
     
        audio=r.listen(source)
    
    try:
        print('recognizing.....')
        query1=r.recognize_google(audio,language='en-in')
        query=query1.lower()
        print(f'user said: {query}')
        return query
    
    except Exception as e:
        print("please say that again")
        return 'none'
    