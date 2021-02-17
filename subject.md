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