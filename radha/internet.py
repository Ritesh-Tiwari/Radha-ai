# importing requests module
import requests
import wikipedia

def check_internet_connection():
    try:
        # requesting URL
        request = requests.get("https://www.google.com", timeout=10)
        return True
    
    # catching exception
    except (requests.ConnectionError,
            requests.Timeout) as exception:
        return False

    return True

def check_on_wikipedia(query):
    query = query.lower()
    query = query.replace('who is',"")
    query = query.replace("what is" ,"")
    query = query.replace("do you know", "")
    query = query.replace("tell me", "" )
    query = query.strip()

    try:
        data = wikipedia.summary(query, sentences = 2)
        print(data)
        return data
    except Exception as e:
        return "None"

# check_on_wikipedia("what is facebook")