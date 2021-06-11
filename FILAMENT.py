import speech_recognition as sr
import pyttsx3
import pyaudio 
import pywhatkit
import datetime
import sys 
import os 
import subprocess





 
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def talk(text):

    engine.say(text)
    engine.runAndWait()

6

def take_command(): 
    command = ''
    
    try:
        with sr.Microphone() as source:
            print("LISTENING....")
            listener.adjust_for_ambient_noise(source,duration=1)
            voice = listener.listen(source,timeout=8,phrase_time_limit=5)
            command = listener.recognize_google(voice,language="en-US")
            listener.pause_threshold = 5
            command = command.lower()
            listener.runAndWait()

    except:
        pass
    return command






def run_filament():


    command=take_command()
    print(command)


    if 'play' in command:
        print('playing')
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt('song')

    elif 'whatsapp message' in command:
        msg = command.replace('whatsapp message ','')
        now = datetime.datetime.now()
        t=now.strftime('%H')
        t1=now.strftime('%M')
        t2=int(t1)
        t3=int(t)
        talk("please enter the phone number")
        phone=input("please enter the phone number\n")
        pywhatkit.sendwhatmsg(phone,msg,t3,t2+2)


    elif 'search' in command:
        searching = command.replace('search','')
        pywhatkit.search(searching)
        talk('searching on your browser')
        print('searching on your browser')

    elif 'date' in command:
        now = datetime.datetime.now()
        print(now.strftime('%Y-%m-%d  %H:%M:%S'))
        talk('here you go')

    elif 'take rest'  in command:
        talk('Alright sir , going for a nap')
        talk('Au revoir')
        print('Au revoir')
        sys.exit()

    #elif 'shutdown' in command:
     #   talk('make your confirmation sir ')
      #  print('make your confirmation sir YES/NO')
       # if 'yes' in command:
        #    os.system('shutdown /s /t 10')
       # else :
        #    exit()

    elif 'search' in command:
        searchengine=command.replace('search','')
        pywhatkit.search(searchengine)
        talk('searching youw browser')
        print('searching your browser')

    elif'shut down' in command:
        talk('PLEASE CONFIRM YOUR COMMAND')
        pywhatkit.shutdown(time=90)
    
    elif 'cancel' and 'shutdown' in command:
        talk('cancelling your process')
        pywhatkit.cancelShutdown()

    elif 'directory c' in command:
        talk('here you go ')
        os.startfile("C:")


    elif '' in command :
        talk('hello sir , are you there?')

    else :
        print('sorry I was busy doing some work can you please repeat')
        talk('sorry I was busy doing some work can you please repeat!!')
    return run_filament()



def verify():

        talk('you have only 1 attempt left')

        talk('please confirm your password')

        command=take_command()
        print(command)


        if 'filament' in command :
            talk("Welcome back sir , Good to see you again")
            run_filament()


        else:
            talk('alert , alert!!!!!!!')
            talk('sending alert msg')
            now = datetime.datetime.now()
            t=now.strftime('%H')
            t1=now.strftime('%M')
            t2=int(t1)
            t3=int(t)
            
            pywhatkit.sendwhatmsg('+919315841307','someone is trying to use filament and access your data',t3,t2+2)
            exit()



def verification():
    talk("Please confirm your password ")
    command=take_command()
    print(command)
    if 'filament' in command :
        talk("Welcome back sir , Good to see you again")
        run_filament()
    else:
        verify()

verification()







