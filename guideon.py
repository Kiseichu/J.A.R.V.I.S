#!/bin/python3
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import os
from dt import date, timeh

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def helloh():
    speak("Bonjour Capitaine !")
    speak("on est le ")
    date()
    speak('a')
    timeh()

def commande():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Donner moi un ordre")
        r.pause_threshold = 1
        r.energy_threshold = 5400
        aud = r.listen(source)
    try:
        print("Ecoute....")
        requete = r.recognize_google(aud, language='fr-FR')
        print(requete)
    except Exception as e:
        print(e)
        speak("S'il vou plait répétez votre commande ...")
        return 'None'
    return requete

def main():
    helloh()
    speak("Formulez votre demande ...")
    while True:
        req = commande().lower()
        if ("heure" in req):
            timeh()
        elif ("date" in req):
            date()
        elif ("fermer" in req):
            exit()
        elif ("wikipédia" in req):
            speak("Recherche en cours ...")
            req = req.replace("wikipédia", "")
            if (req == ""):
                continue
            wikipedia.set_lang("fr")
            try:
                res = wikipedia.summary(req, sentences=2)
                speak(res)
            except wikipedia.exceptions.PageError:
                speak("Error dans Wikipédia")
                continue
            except wikipedia.exceptions.HTTPTimeoutError:
                speak("Erreur 42")
                continue
        elif ("ferme ta gueule" in req):
            speak("pas besoin d'autant de violence")
            exit(0)

if (__name__ == "__main__"):
    main()