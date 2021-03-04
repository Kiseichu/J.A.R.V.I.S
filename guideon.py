#!/bin/python3
#Import for step 1
import playsound, tempfile, gtts
#Import for step 2
import datetime, time
#Import for step 3
import speech_recognition, locale
#Import for step 4
import wikipedia
#import for step 5
import webbrowser as wb
#Import for step 6
import os
#Import for Step 8
import psutil

Ai_name = "Guideon"

def say(audio):
    speech = gtts.gTTS(text=audio, lang="fr")
    tmp = tempfile.NamedTemporaryFile()
    speech.write_to_fp(tmp.file)
    playsound.playsound(tmp.name)
    tmp.close()

def rec_voice():
    rec = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Recording")
        rec.pause_threshold = 1
        rec.energy_threshold = 5400
        voice = rec.listen(source)
        try:
            result = rec.recognize_google(voice, language='fr_FR')
        except:
            say("Je n'ai pas compris Idiot")
            print("No result")
            result = None
        return result

def rec_loop():
    result = None
    while result == None:
        result = rec_voice()
        time.sleep(1)
    return result.lower()

def say_date():
    locale.setlocale(locale.LC_TIME, "fr_FR")
    current_date = datetime.datetime.now().strftime("%A %d %B %Y %H:%M")
    say(current_date)

def wikiped(request):
    say("Recherche en cours ...")
    if (request == ""):
        say("Rien pour wikipedia")
        return
    wikipedia.set_lang("fr")
    try:
        res = wikipedia.summary(request, sentences=2)
        say(res)
    except:
        say("Erreur 404")
        return

def system_interaction(result):
    if (result == "verrouiller"):
        say("Vérouillage de l'ordinateur en cours ...")
        os.system("qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock")
    elif (result == "arrêter"):
        say("Arret system")
        os.system("poweroff")
    elif(result == "redémarrer"):
        say("Redémarage en cours ...")
        os.system("shutdown -r -t 0")

def play_musique():
    song_path = "/home/khadafi/Music"
    song_list = os.listdir(song_path)
    for i in range(len(song_list)):
        os.system("mpg123 " + os.path.join(song_path, song_list[i]))

def write_note():
    say("Que voulez vous retenir ?")
    rappel = rec_voice()
    say("Vous m'avez demander de retenir :" + rappel)
    y_n = rec_voice()
    filetxt = open("./save/note.txt", "w")
    filetxt.write(rappel)
    filetxt.close()

def read_note():
    filetxt = open("./save/note.txt", "r")
    say("Vous m'avez demander de retenir :")
    say(filetxt.read())

def infocomputer():
    lvlProc = str(psutil.cpu_percent())
    say(lvlProc+"Poucentage utiliser par le processeur")
    lvlbat = str(psutil.sensors_battery().percent)
    say(lvlbat + "pourcent de batterie")

if __name__ == "__main__":
    say("Bonjour capitaine !")
    while True:
        say("Je vous écoute ...")
        result = rec_loop()
        word_array = result.split()
        print(word_array)
        if (word_array[0] == "fermer"):
            exit(0)
        elif (word_array[0] == "date"):
            say_date()
        elif (word_array[0] == "c'est" and (word_array[1] == "quoi" or word_array[1] == "qui")):
            wikiped(word_array[2])
        elif (word_array[0] == "internet"):
            say("Le site sur lequelle vous voulez allez ...")
            link = rec_voice()
            google_path = "/usr/bin/google-chrome %s"
            wb.get(google_path).open_new_tab(link)            
        elif (word_array[0] == "musique"):
            play_musique()
        elif (word_array[0] == "noter"):
            write_note()
        elif ("note" in result):
            read_note()
        elif (word_array[0] == "capture" and word_array[1] == "d'écran"):
            os.system("ffmpeg -f x11grab -r 25 -s 1920x1080 -i :0.0 /home/khadafi/delivery/J.A.R.V.I.S/save/cap.png")
            say("Capture d'écran terminer")
        elif ("système" in result):
            infocomputer()
        system_interaction(word_array[0])

        
