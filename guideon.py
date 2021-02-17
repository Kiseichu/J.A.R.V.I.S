#!/bin/python3
import smtplib, ssl, wikipedia, pyttsx3, datetime, os
import speech_recognition as sr
import webbrowser as wb
import pyautogui, psutil
from dt import date, timeh

smtp_mail = 'smtp.gmail.com'
smtp_port = 586

email_adress = 'thecollonelz@gmail.com'
email_passwd = '***************'

Ai_name = "Guideon"

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

def wikiped(request):
    speak("Recherche en cours ...")
    if (request == ""):
        speak ("Rien pour wikpéddia")
        return 84
    wikipedia.set_lang("fr")
    try:
        res = wikipedia.summary(request, sentences=2)
        speak(res)
    except wikipedia.PageError:
        speak("Pas d'internet")
        return 84

def mail(box):
    with smtplib.SMTP(smtp_mail, smtp_port) as server:
        server.starttls()
        server.login(email_adress, email_passwd)
        try:
            server.sendmail(email_adress, 'hadjeekhadafi@outlook.com', box)
            speak("Email envoyer !")
        except Exception as e:
            print(e)
            speak("Email refusé !")
        server.close()

def capture():
    image = pyautogui.screenshot()
    image.save("C:\\Users\\hadje\\Documents\\Jarvis\\J.A.R.V.I.S\\cap.png")

def infocomputer():
    lvlProc = str(psutil.cpu_percent())
    speak(lvlProc+"Poucentage utiliser par le prcesseur")
    lvlbat = str(psutil.sensors_battery().percent)
    speak(lvlbat + "pourcent de batterie")

def main():
    #helloh()
    speak("Formulez votre demande ..."),
    while True:
        req = commande().lower()
        if ("heure" in req):
            timeh()
        elif ("date" in req):
            date()
        elif ("fermer" in req):
            exit()
        elif ("wikipédia" in req):
            req = req.replace("wikipédia", "")
            if (wikiped(req) == 84):
                continue
        elif ("ferme ta gueule" in req):
            speak("pas besoin d'autant de violence")
            exit(0)
        elif ("internet" in req):
            speak("Donne moi l'adresse du site internet")
            lien = commande()
            chemin = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            wb.get(chemin).open_new_tab(lien)
        elif ("déconnecter" in req):
            os.system("shutdown -l")
        elif ("arrêter l'ordinateur" in req):
            os.system("shutdown -s -t 0")
        elif ("redémarrer" in req):
            os.system("shutdown -r -t 0")
        elif ("musique" in req):
            song_path = "C:/Users/hadje/Music"
            song_list = os.listdir(song_path)
            for i in range(len(song_list)):
                os.startfile(os.path.join(song_path, song_list[i]))
        elif ("noter" in req):
            speak("Que faut t-il retenir pour vous ?")
            rappel = commande()
            speak("Vous m'avez demander de retenir :" + rappel)
            filetxt = open("note.txt", 'w')
            filetxt.write(rappel)
            filetxt.close()
        elif ("lire" in req):
            filetxt = open("note.txt", 'r')
            speak("Vous m'avez demander de retenir :")
            speak(filetxt.read())
        elif ("capture d'écran" in req):
            capture()
            speak("La capture d'écran est términer")
        elif ("système" in req):
            infocomputer()

if (__name__ == "__main__"):
    main()