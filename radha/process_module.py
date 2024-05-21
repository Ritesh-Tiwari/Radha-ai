import random
from output_module import output
from time_module import get_time, get_date
from database import *
from input_module import take_input
from internet import check_internet_connection, check_on_wikipedia
import assistant_details
from web_job import *
from music import *
from news import get_news
from word_bank import *
from weather_report_module import get_weather_report
from todo_module import TodoMoudle
def process(query):

    if "radha" in query.lower():
        query = query.replace('radha','')
        query = query.strip()

        #  when some one greet radha 
        if any(greeting in query.lower() for greeting in hello_list):
            output("Hello Sir, how can I help you?")
            ans = take_input()
            data = process("radha "+ ans)
            return data


        
        answer = get_ans_from_memory(query)
        
        if answer == "tell date" or 'the date' in query.lower():
            return "Date is " + get_date()
        
        elif any(i in query.lower() for i in thank_you_list):
            return random.choice(respond_to_thank_you_list)
        
        elif "weather report" in query.lower():            
            return get_weather_report()
        
        elif answer == "tell time" or 'the time' in query.lower() :
            return "Sir, time is " + get_time()

        elif answer == "check internet connection":
        
            if check_internet_connection():
                return "internet is connected."
            else :
                return "internet is not connected"
        
        elif answer == "on speak":
            return turn_on_speech()

        elif answer == "off speak":
            return turn_off_speech()

        elif answer == "open facebook":
            open_facebook()
            return "opening facebook"
        
        elif answer == "open google":
            open_google()
            return "opening google"
        
        elif answer == "open browser":
            open_google()
            return "opening browser"
        elif answer == "close browser":
            close_browser()
            return "closing browser"
        elif answer == "play music":
            return play_music()
        
        elif answer == "pause music":
            return pause_music()
        
        elif answer == "stop music":
            return stop_music()
        
        elif answer == "next song":
            return next_song()
        
        elif answer == "previous song":
            return previous_song()
        
        elif answer == "play":
            return play_specific_song(query)

        elif answer == 'get news':
            return get_news()
        
        elif answer == "change name":
            output ("Okay! what to you want to call me")
            temp = take_input()
            if temp == assistant_details.name:
                return "Can't change. Its jusy my prevois name"
            else:
                update_name(temp)
                assistant_details.name = temp
                return "Now you can call me "+ temp
        
        elif answer == "get all to do":
            output ('Okay Sir, connecting your to do list')
            todos = TodoMoudle.get_all_todo()
            for i in todos:
                return f"id {i[0]}, task name {i[1]}, due date {i[2]} and status {i[3]}"


        else:
            if answer == "":
                output("Don't know this one should i search on internet ?")
                yes_or_no = take_input()
                
                if 'yes' in yes_or_no.lower() or 'ok' in yes_or_no.lower() or "okay" in yes_or_no.lower():
                    answer = check_on_wikipedia(query)
                    if answer != "":
                        return answer
            
                
                else:
                    output("can you please tell me what is it mean ?")
                    ans = take_input()
                    lists = ["it's means", "it means"]

                    for i in lists:
                        if i in ans:
                            ans = ans.replace(i,'')                        
                            ans = ans.strip()
                            value = get_ans_from_memory(ans)

                            if value == "":

                                return "can't help with this one"
                            else:
                                insert_question_and_answer(query, value)
                                return "Thanks i will remember it for the next time"
                        else:
                            return "can't help with this one"

    else:
        return "ignore"