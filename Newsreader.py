import time
import requests
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Voice = speak.GetVoices().Item(1)
    speak.Speak(str)

url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'sortBy=popularity&'
       'apiKey=dd6d74b5b92e45c28006db5038fafa74')
r = requests.get(url)
articles = r.json()['articles']

for i in range(10):
    news = r.json()['articles'][i]['title']
    news = news.split(" - ", 1)[0]
    speak(f"Headline {i+1}")
    speak(news)
    time.sleep(1)
