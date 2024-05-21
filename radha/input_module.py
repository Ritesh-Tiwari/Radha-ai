from assistant_details import name
import speech_recognition as sr # for add commands

def take_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio=r.listen(source,timeout=8,phrase_time_limit=8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n ")

    except sr.UnknownValueError:
        return "Could not understand audio, Please say it again..."
    
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "None"    
    return query



