#!/bin/python3

import pyttsx3
import datetime

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def timeh():
    h = datetime.datetime.now().strftime('%I:%M')
    hour = int(datetime.datetime.now().hour)

    speak(h)
    if (hour >= 0 and hour <= 12):
        speak("du matin")
    else:
        speak("de l'aprem")

def weekday(week):
    if (week == 0):
        speak("Lundi")
    elif (week == 1):
        speak("Mardi")
    elif (week == 2):
        speak("Mercredi")
    elif (week == 3):
        speak("Jeudi")
    elif (week == 4):
        speak("Vendredi")
    elif (week == 5):
        speak("Samedi")
    else:
        speak("Dimanche")

def monthname(monthnm):
    if (monthnm == 1):
        speak("Janvier")
    elif (monthnm == 2):
        speak("Fevrier")
    elif (monthnm == 3):
        speak("Mars")
    elif (monthnm == 4):
        speak("Avril")
    elif (monthnm == 5):
        speak("Mai")
    elif (monthnm == 6):
        speak("Juin")
    elif (monthnm == 7):
        speak("Juillet")
    elif (monthnm == 8):
        speak("Aout")
    elif (monthnm == 9):
        speak("Septembre")
    elif (monthnm == 10):
        speak("Octobre")
    elif (monthnm == 11):
        speak("Novembre")
    else:
        speak("Décembre")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    dayn = int(datetime.datetime.now().day)
    day = int(datetime.datetime.now().weekday())

    weekday(day)
    speak(dayn)
    monthname(month)
    speak(year)