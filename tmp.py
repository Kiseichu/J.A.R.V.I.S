def speak(audio):
    speech = gtts.gTTS(text=str(audio), lang="fr")
    tmp = tempfile.NamedTemporaryFile()
    speech.write_to_fp(tmp.file)
    playsound.playsound(tmp.name)
    tmp.close()

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

def capture():
    image = pyautogui.screenshot()
    image.save("/home/khadafi/delivery/J.A.R.V.I.S/save/cap.png")

def infocomputer():
    lvlProc = str(psutil.cpu_percent())
    speak(lvlProc+"Poucentage utiliser par le prcesseur")
    lvlbat = str(psutil.sensors_battery().percent)
    speak(lvlbat + "pourcent de batterie")

def main():
    helloh()
    speak("yo quoi de neuf bitch"),
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
            os.system("qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock")
        elif ("arrêter l'ordinateur" in req):
            os.system("poweroff")
        elif ("redémarrer" in req):
            os.system("shutdown -r -t 0")
        elif ("musique" in req):
            song_path = "/home/khadafi/Music"
            song_list = os.listdir(song_path)
            for i in range(len(song_list)):
                os.system("vlc " + os.path.join(song_path, song_list[i]))
        elif ("noter" in req):
            speak("Que faut t-il retenir pour vous ?")
            rappel = commande()
            speak("Vous m'avez demander de retenir :" + rappel)
            filetxt = open("./save/note.txt", 'w')
            filetxt.write(rappel)
            filetxt.close()
        elif ("lire" in req):
            filetxt = open("./save/note.txt", 'r')
            speak("Vous m'avez demander de retenir :")
            speak(filetxt.read())
        elif ("capture d'écran" in req):
            os.system("ffmpeg -f x11grab -r 25 -s 1920x1080 -i :0.0 /home/khadafi/delivery/J.A.R.V.I.S/save/cap.png")
            speak("La capture d'écran est términer")
        elif ("système" in req):
            infocomputer()

if (__name__ == "__main__"):
    main()