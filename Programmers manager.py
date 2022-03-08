import os
import time
from datetime import datetime, timedelta
import pygame
from pygame import mixer

print("Welcome...", os.getlogin())


def now():
    now=datetime.now()
    return now.strftime("%d/%m/%y %H:%M:%S")

def water():
    pygame.mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.play(-1)
    print("Please drink water")
    time.sleep(5)
    while True:
        query = input("Enter:Drank after drinking water").lower()
        if query == 'drank':
           mixer.music.stop()
           file=open("water.txt",'a')
           file.write(f"{now()} Water")
           file.write("\n")
           file.close()
           break

def eyes():
    pygame.mixer.init()
    mixer.music.load("eye.mp3")
    mixer.music.play(-1)
    print("Please relex your eye")
    time.sleep(5)
    while(True):
        query=input("Enter:OK after eye relexing").lower()
        if query == "ok":
            mixer.music.stop()
            file=open("eye.txt","a")
            file.write(f"{now()}Eye Relex")
            file.write("\n")
            file.close()
            break

def excersize():
    mixer.init()
    mixer.music.load("excer.mp3")
    mixer.music.play(-1)
    print("Please do light workout.")
    time.sleep(5)
    while(True):
        query=input("Enter:Done after light body excersize").lower()
        if query=="done":
            mixer.music.stop()
            file=open("excer.txt","a")
            file.write(f"{now()}Excersize done")
            file.write("\n")
            file.close()
            break

while (True):
    a = input("Please press enter to start your clock")
    if a == "":
        print("Manager activeted")
        t=datetime.now()
        lastw=datetime.now()
        laste = datetime.now()
        lastx = datetime.now()

        while(True):

            current=datetime.now()

            if current>=lastw+timedelta(minutes=30):
                water()
                lastw=lastw+timedelta(minutes=30)

            if current>=laste+timedelta(minutes=30):
                eyes()
                laste=laste+timedelta(minutes=30)

            if current>=lastx+timedelta(minutes=45):
                excersize()
                lastx=lastx+timedelta(minutes=45)

            if current>t+timedelta(hours=8):
                break

        break
    else:
        print("Please press enter")

print("Great workday over...Singing off.")