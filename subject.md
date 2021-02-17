# How to create J.A.R.V.I.S

## Description

Vous avez déjà entendue parler de la fameuse artificielle intelligente *J.A.R.V.I.S*.

Aujourd'hui dans ce workshop vous allez apprendre a récréer cette intelligence artificielle.

Tous ce passeras sur la platform Windows 10 avec python et quelque autre module.

## Step 1

Vous allez commencer par faire parler Jarvis en utilisant et installant le module : **pyttsx3**.

    >>> pip install pyttsx3

Et ensuite créer une fonction avec en parametre votre audio :

    import pyttsx3

    def speak(audio):
        # on vas initier le module et lui donner une variable
        engine = pyttsx3.init()
        # on vas le donner l'audio pour le faire parler
        engine.say(audio)
        # et ensuite le demandais de l'executer et d'attendre
        engine.runAndWait()

Après avoir fait ça vous pouvez donner ce que vous voulez pour faire parler Jarvis.

## Step 2

Maitenant que vous pouvez faire parler Jarvis on vas lui faire dire la date et 
l'heure on le recuperant avec le module : **datetime**, si vous ne l'avait installer le :

    >>> pip install datetime

et vous allez recupérer le *mois*, *l'année* et *jour*.

    import datetime

    # Sa vas être la même pour les autre variable
    year = int(datetime.datetime.now().year)

Après avoir récupérer l'heure vous allez devoir lui dire si c'est le *matin*, *l'après-midi* ou le *soir*.

## Step 3

On vas donc commencer a parlez avec Jarvis pour ceci on vas avoir 
besoin de quelque modules : **pipwin**, **pyaudio** et
**speechrocognition**.

    >>> pip install pipwin
    >>> pipwin install pyaudio
    >>> pip install speechrocognition

Vous allez donc créer une fonction qui vas permettre de récupérer votre voix :

    # On fait importer speech_recognition on lui donne un nom plus cour pour l'appeler
    import speech_recognition as sr
    def rec_voice():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            speak("Donnez moi un ordre ...")
            r.pause_threshold = 1
            r.energy_threshold = 5400
            voice = r.listen(source)
            # Avec tout sa sa vas nous permettre de recupérer notre voix
        try:
            request = r.recognize_google(voice, language='fr-FR')
            print(request)
        except Exception as e:
            print(e)
            speak("Je n'ai pas compris votre demande reformulez la ...")
            return 'None'
        return request

Avec tous vous pouvez enfin parler un *Jarvis*.

## Step Bonus

Dans cette step on vas rien apprendre de plus juste on vas réorganiser notre 
code avec un main:

    #!/bin/python3
    import pyttsx3
    import datetime
    import speech_recognition as sr

    # La fontion qui permet de parler
    def speak(audio):
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()

    # La fonction qui donne l'heure
    def timeh():
    h = datetime.datetime.now().strftime('%I:%M')
    hour = int(datetime.datetime.now().hour)
    speak(h)
    if (hour >= 0 and hour <= 12):
        speak("du matin")
    else:
        speak("de l'aprem")
    
    # La fonction qui donne la date
    def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    dayn = int(datetime.datetime.now().day)

    speak(dayn)
    speak(month)
    speak(year)

    # Une petite fonction de salution
    def helloh():
    speak("Salut on est le ")
    date()
    speak('a')
    time()

    # La fonction qui permet de récupérer la voix
    def rec_voice():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            speak("Donnez moi un ordre ...")
            r.pause_threshold = 1
            r.energy_threshold = 5400
            voice = r.listen(source)
            # Avec tout sa sa vas nous permettre de recupérer notre voix
        try:
            request = r.recognize_google(voice, language='fr-FR')
            print(request)
        except Exception as e:
            print(e)
            speak("Je n'ai pas compris votre demande reformulez la ...")
            return 'None'
        return request
    
    # La fonction principale
    def main():
    helloh()

    while True:
        request = rec_voice().lower()
        # Ce if chercher si dans request il y a heure
        if ("heure" in request):
            timeh()
        elif ("date" in req):
            date()
        elif ("fermer" in req):
            exit()
    
    # Ici on définie la fonction principal qui est le main
    if (__name == "__main__"):
        main()

Voià maintenant que votre code est réorganiser on vas pouvoir passer 
a la suite.

## Step 4

On vas passez au chose plus intéressante a savoir faire des recherche sur 
wikipédia avec le module : **wikipedia**.

    >>> pip install wikipedia

On vas donc créer la condtion qui vas permettre de faire des recherche sur 
wikipédia mais d'abord vous vous allez rajouter ceci dans la *fonction main* 
après les elif :

    elif (wikipedia in request):
        # Il vas remplacer wikipédia par rien
        request = request.replace("wikipédia", "")
        if (wikiped(request) == 84):
            continue

On vas du coup passer à la fonction qui permet de faire la recherche sur 
wikipédia:

    def wikiped(request):
        if (request == ""):
            return 84;
        wikipedia.set_lang("fr")
        # Du coup ici on vas tester si sa marche ou pas
        try:
            res = wikipedia.summary(req, sentences=2)
            speak(res)
        except wikipedia.exceptions.PageError:
            speak("HTTP error")
            return 84

Voila maintenant vous pouvez demander a Jarvis de faire des recherches sur 
wikipedia pour vous.

J'espere que vous etes encore là et si oui on vas passer a la suite.

## Step 5

On vas maintenant ouvrir un site web une etape trés facile.
On vas utilisé le module : **webbroser** qui est déjà installer sur votre ordi.

Pour ouvrir un site web il nous faut le chemin de l'èxecutable de votre 
navigateur par default (pour moi c'est chrome). Et on vas tout rajouter dans le main.

    import webbroser as wb

    elif (request == "internet"):
        speak("Donner moi le nom du site internet")
        link = req_voice()
        path = "chemin de l'èxecutable de votre navigateur par default"
        wb.get(path).open_new_tab(link)

Maintenant vous pouvez ouvrir un site internet pratique n'est ce pas.
Essayer avec twitter.com par exemple.

## Step 6

Maintenant on vas voir pour *Arrêter*, se *décconnecter* et *redémarrer* l'ordinateur 
avec le module : **os**.

On vas donc rajouter c'est 6 lignes de code dans le main:

    import os

    elif ("déconnecter" in req):
        os.system("shutdown -l")
    elif ("arrêter l'ordinateur" in req):
        os.system("shutdown -s -t 0")
    elif ("redémarrer" in req):
        os.system("shutdown -r -t 0")

Encore une étape facile n'est-ce-pas ?

## Step 7

Encore une étape facile vous inquiéter pas !! on vas jouer de la musique a partir d'un dossier toujours avec le module : **os**.

Vous allez avoir besoin du chemin de votre fichier de musique qu'il faudra mettre dans une variable.
Vous allez pour cela rajouter encore dans votre main:

    elif ("musique" in request):
        song_path = "chemin du fichier de musique*
        song_list = os.listdir(song_path)
        for i in range(len(song_list)):
            # le os.path.join c'est une sort de strcat qui assemble 2 string
            os.startfile(os.path.join(song_path, song_list[i]))

Et voila pour la musique. Encore trop simple n'est ce pas.


## Step 8

Maintenant on vas apprendre à créer une note et le faire lire par *Jarvis*.
Pour cela vous allez devoir ajouter à votre main:

    # Ici on vas mettre dans un fichier qu'est ce que vous voulez retenir
    elif ("noter" in request):
        speak("Que faut t-il retenir pour vous")
        reminder = rec_voice()
        speak("Vous voulez me faire retenir" + reminder)
        # Si note.txt n'existe pas vous inquiéter pas il vas le créer pour vous
        filetxt = open("note.txt", 'w')
        filetxt.write(reminder)
        filetxt.close()
    # Et ici on vas le faire lire
    elif ("rappel" in request):
        filetxt = open("note.txt", 'r')
        speak("Vous m'avez demander de retenir :")
        speak(filetxt.read())

Comme vous pouvez le voir ici on a déjà un fichier pré-définis. Mais après avoir 
comment coller 2 string ensemble mais aussi replacer dans la string. Vous pouvez allez 
plus loin en donner a Jarvis le fichier dans laquel vous voulez écrire et lire.

## Step 9

Sa faisait longtemps on a pas installer de nouveau module bon pour cette partie vous aurez besoin de : **pyautogui**.

    >>> pip install pyautogui

Avec ce module et dans cette partie on vas pouvoir faire des capture d'écran.

Pour cela vous allez avoir besoin d'une nouvelle fonction et d'un chemin pour sauvegardez votre image:

    def capture():
        img = pyautogui.screenshot()
        speak("Donnez le nom de votre img avec son extension")
        name_of_file = rec_voice()
        img.save("le chemin" + name_of_file)

Et vous ajouterais cette fonction dans le main avec bien entendue et comme 
d'habitube une condition *elif*.

## Step 10

On est enfin a la derniere étape et cette étape consiste a avoir les info
de la batterie mais aussi su processeur.

Du coup nouveau module qui est : **psutil**.

    >>> pip install psutil

Et pour récuperer le pourcentage de batterie et du processeur on vas avoir besoin de la 
fonction suivantes:

    def infocomputer():
    # lvlProc qui est le poucentage de batterie
    lvlProc = str(psutil.cpu_percent())
    speak(lvlProc+"Poucentage utiliser par le prcesseur")
    # lvlbat qui correspond au pourcentage de batterie
    lvlbat = str(psutil.sensors_battery().percent)
    speak(lvlbat + "pourcent de batterie")

Evidemment vous ajouterais cette fonction à votre main.
Avec et toujours des *elif*.

# BONUS

Bravo à vous, d'etre arriver jusqu'ici. Vous avez enfin le temps de arranger votre code 
et oui sa fait beaucoup d'elif que vous avez la!

Je peux vous proposer d'autre truc a faire si vous voulez allez plus loin avec Jarvis:
* Permettre a Jarvis d'envoyer un email a n'importe qu'elle destinataire.
* Faire des requete HTTP sur l' intranet d'Epitech pour soit vous inscrire une 
activités, récuperer votre emploi du temps etc ...
* Vous pouvez annalyser aussi la sécurité sur votre ordinateur comme les pare-feu etc..

En gros vous avez une possibilités infinie, Votre Jarvis resteras votre Jarvis si vous partez 
au bout de la chose

Merci pour m'avoir suivi tout au long de ce workshop et au plaisir de vous revoirs.