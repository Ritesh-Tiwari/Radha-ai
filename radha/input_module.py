from assistant_details import name
import speech_recognition as sr # for add commands

def take_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
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



