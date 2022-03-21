import sys
import os
import requests
import string
import re
import webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver


''' fetching subtitle of a movie -- for windows

1. Need to add the program to the right click features
2. Need to select the folder/movie file and then execute the program
3. The corresponding subtitle of movie will be downloaded
'''

def openpage(wiki):
            linklist = []
            wiki.replace(" ", "")
            wiki = wiki.strip();
            #print(wiki)
            url = 'https://www.google.co.in/search?q='+wiki+'+english subtitle subscene'
            #print(url)
            r = requests.get(url)
            k = r.text
            #print(k)
            m = re.search('https://subscene.com/subtitles/(.+?)/english/(.+?)+', k)
            #print(m)
            if m:
                link = m.group(0)
                link = link.split('&amp')
                #print(link[0])
            #return 10
            
            r = requests.get(link[0])
            k = r.text            
            
            
            
            soup1 = BeautifulSoup(k,"html.parser")
            
            div=soup1.find(id='downloadButton')
            downloadd='https://subscene.com/'+ div['href']
            
            
            

            
            options = webdriver.ChromeOptions()
            dow=os.getcwd()
            
            #print(download.default_directory)

            prefs = {'download.default_directory' : dow}
            options.add_experimental_option('prefs', prefs)
           
            options.add_argument("--disable-infobars")

            driver = webdriver.Chrome()
            options=webdriver.Chrome('C:\Webdrivers\chromedriver.exe',chrome_options=options)
            options.get(downloadd)
            
            #webbrowser.open(downloadd)
            #print(os.getcwd())
wiki = sys.argv[1]
wiki = wiki.split("\\")
#print(wiki)
openpage(wiki[len(wiki)-1])
#openpage('The Dinner 2017')            
