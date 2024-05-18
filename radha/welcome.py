from time_module import get_hours, get_date
from output_module import output
from database import updates_last_seen,get_last_seen
from datetime import date

def greet():

    # fetch previous date and store it to database
    previous_date = get_last_seen()

    # fetch today's date and store it to database
    today_date = get_date() 
    updates_last_seen(today_date)

    hour = int(get_hours())
    
    if previous_date == today_date :
        output("Welcome back, Sir ")

    else:
        if hour > 4 and hour < 12:
            output ("Good Morning, Sir")
    
        elif hour >=12 and hour <16 :
            output ("Good After Noon, Sir")

        else :
            output ("Good Evening, Sir")


