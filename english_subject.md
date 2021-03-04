# How to create J.A.R.V.I.S

## Description

You've already heard about the famous artificial intelligent **J.A.R.V.I.S** in
the film Iron-man.

Today in this workshop you will learn how to recreate this artificial intelligence.

All this will with python and some other modules.

## Installion

For the installation in your terminal you nedd to tap:

    pyenv venv .
    sudo dnf install python-devel espeak portaudio portaudio-devel
    touch requirement.txt

In *requirement.txt* you need to tap every module you need for exemple:

    gtts
    pyaudio
    speechrecognition

After:
    source bin/activate
    sudo pip install -r requirement.txt

And now you can start to code.

## Step 1

For the begining, you need to use the module : **gtts** to computer talk.

Write a function that make jarvis talk.

## Step 2

For the second step, you need to use **datetime** module to get the 
time and the day of today.

And with *gtts* say it.

## Step 3

Now, one of the most important part you need that Jarvis recognize your voice
we need modules : **pyaudio** et
**speechrocognition**.

You create a fonction that recognize your voice and print or just let 
Jarvis say it.

## Step Bonus

In this bonus step you need to orgonize your code like that with the **main** 
fonction:

#!/bin/python3

#Import for step 1
import playsound, tempfile, gtts
#Import for step 2
import datetime, time
#Import for step 3
import speech_recognition, locale
#Import for step 4
import wikipedia

Ai_name = "Guideon"

def say(audio):
    speech = gtts.gTTS(text=audio, lang="fr")
    tmp = tempfile.NamedTemporaryFile()
    speech.write_to_fp(tmp.file)
    playsound.playsound(tmp.name)
    tmp.close()

def rec_voice():
    say("Je vous ecoute ...")
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

if __name__ == "__main__":
    say("Bonjour capitaine !")
    while True:
        result = rec_loop()
        word_array = result.split()
        print(word_array)
        if (word_array[0] == "fermer"):
            exit(0)
        elif (word_array[0] == "date"):
            say_date()

Voià maintenant que votre code est réorganiser on vas pouvoir passer 
a la suite.

## Step 4

In this step we go to research in wikipedia with the module name: **wikipedia**.
When you talk with jarvis and you say : "wikipedia bill gates", you need 
to transform your string in lowercase and delete the word 
"wikipedia" and resume bill gates, for exemple,in 2 sentences.

I hope you're still here and if so we'll move on.

## Step 5

Now an easy step with the module : **webbroser**, we go in your default application
web broser and you say to jarvis you want to open a website like "twitter.com"
tt opens a new tab in twitter.com, for exemple.

## Step 6

Another easy step with the module **os**, you need to tell at Jarvis that you want to shutdown,
lock or reboot your computer.

Another easy step, isn't it?

## Step 7


One more easy step, don't worry, we will play music from a folder always with the : **os** module.
I let you do that.

You need to have the path of the music file. And use for exemple *vlc* or *mpg123*.


## Step 8

Now we will learn how to create a note and make *Jarvis* read it.

As you can see here we already have a predefined file. But after having how 
to paste 2 strings together
but also put them back in the string. You can go further and give Jarvis the 
file you want to write to and read from.

## Step 9

It's been a long time we haven't installed a new module good for this part you'll need : **pyautogui**.

    >>> pip install pyautogui

With this module and in this part we will be able to make screenshots.

## Step 10

We are finally at the last stage and this stage consists in having the information
of the battery but also of the processor.

Therefore, a new module which is : **psutil**.

    >>> pip install psutil

# BONUS

Congratulations to you for getting here. You finally have time to fix your code. 
and yes it makes a lot of elif that you have there!

I can suggest you other things to do if you want to go further with Jarvis:
* Allow Jarvis to send an email to anyone she wants.
* Make HTTP requests on the Epitech intranet to either subscribe to a 
activities, get your schedule back etc ...
* You can also analyze the security on your computer like firewalls etc...

Basically you have infinite possibilities, Your Jarvis will remain your Jarvis if you leave. 
at the end of the thing

Thank you for following me throughout this workshop and I look forward to seeing you again.