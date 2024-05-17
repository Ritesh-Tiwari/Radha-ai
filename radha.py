import datetime
import pyttsx3 # for voice
import speech_recognition as sr # for add commands
import wikipedia
import webbrowser
import vlc
import os
import subprocess # for terminal use
import smtplib



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[29].id)
engine.setProperty('rate',150)

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    wish me 
    '''
    hour  = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <12 :
        speak("Good Morning !")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening !");

    speak( "I am Radha. Please tell me how may i help you Sir?")

def takeCommand():
    '''
    add commands
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 800
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n ")
        
    except Exception as e :
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("parthadm0514@gmail.com","tpznbekusqvfeyvs")
    server.sendmail("parthadm0514@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while(True):
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            # Register a custom browser with its command
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('/usr/bin/google-chrome'))

            # Open URL in the specified browser (in this case, Firefox)
            webbrowser.get('chrome').open('https://www.youtube.com')
        
        elif 'open google' in query:
            # Register a custom browser with its command
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('/usr/bin/google-chrome'))

            # Open URL in the specified browser (in this case, Firefox)
            webbrowser.get('chrome').open('https://www.google.com')
        
        elif 'open git' in query:
            # Register a custom browser with its command
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('/usr/bin/google-chrome'))

            # Open URL in the specified browser (in this case, Firefox)
            webbrowser.get('chrome').open('https://www.git.com')
        
        elif 'play music' in query:
            music_file = '/home/avcdev/Desktop/old_Farz-Hum To Tere Aashiq.mp3'
            instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

            # Create media player
            player = instance.media_player_new()

            # Load the MP3 file
            media = instance.media_new(music_file)
            player.set_media(media)

            # Start playing
            player.play()

            # Wait for playback to finish
            while player.is_playing():
                pass
        elif 'stop music' in query:
            player.stop()

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strtime}")
            print(f'Sir, The time is {strtime}')
        elif 'open code' in query:
            print("opening vs code")
            subprocess.run('code')
            speak("opening vscode")
        elif 'email to ritesh' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "tiwariritesh989@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            
            except Exception as e:
                print(e)
                speak("Sorry i am not able to send this email")