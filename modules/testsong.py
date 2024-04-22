import requests
from bs4 import BeautifulSoup
from googlesearch import search
import pandas as pd
import re
import os
import pyglet
import time
import speech_recognition as sr
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
                print('present')
                print(website.loc[row,'string'])
                content_finder=soup.find(string=website.loc[row,'string'])
                main_link=content_finder.findParent('a')
                url1=main_link.get('href')
                return url1
            except:
                return 'sorry'
                exit()
def download_sound(a):
    
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
            return print('sorry')
            exit()
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
        return print('song downloaded')

time1=time.time()
download_sound('closer')
time2=time.time()-time1
print(time2)
# download_sound('kaam 25')
