import assistant_details
from speak_module import speak
from database import speak_is_on


def output(o):

    # print command line
    print (assistant_details.name +" : " + o)
    print()

    if speak_is_on():
        speak(o)