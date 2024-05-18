import webbrowser
import os



def open_facebook():
    webbrowser.open('https://www.facebook.com')


def open_google():
    webbrowser.open('https://www.google.com')

def close_browser():
    os.system('pkill chrome')