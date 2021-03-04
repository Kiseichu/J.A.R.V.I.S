#!/bin/python3

import pyttsx3
import datetime
import gtts, tempfile, playsound

def speak(audio):
    speech = gtts.gTTS(text=audio, lang="fr")
    tmp = tempfile.NamedTemporaryFile()
    speech.write_to_fp(tmp.file)
    playsound.playsound(tmp.name)
    tmp.close()

def timeh():
    h = datetime.datetime.now().strftime('%I:%M')
    hour = str(int(datetime.datetime.now().hour))

    speak(h)
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour <= 12):
        speak("du matin")
    elif (hour <= 19):
        speak("de l'aprem")
    else:
        speak("Du soir")

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
    month = int(datetime.datetime.now().month())
    dayn = int(datetime.datetime.now().day)
    day = int(datetime.datetime.now().weekday())

    dayn = str(dayn)
    weekday(day)
    print("je suis pas encore stupide")
    print("Je suis stupide")
    monthname(month)
    speak(year)

def helloh():
    speak("Bonjour Capitaine !" + "On est le ")
    print("lol")
    date()
    print("lol")
    speak("à")
    timeh()