from output_module import output
from time_module import get_time, get_date
from database import get_ans_from_memory, insert_question_and_answer,update_name
from input_module import take_input
from internet import check_internet_connection, check_on_wikipedia
import assistant_details


def process(query):
    answer = get_ans_from_memory(query)

        
    if answer == "tell date":
        return "Date is " + get_date()
        
    elif answer == "check internet connection":
    
        if check_internet_connection():
            return "internet is connected."
        else :
            return "internet is not connected"
    
    elif answer == "change name":
        output ("Okay! what to you want to call me")
        temp = take_input()
        if temp == assistant_details.name:
            return "Can't change. Its jusy my prevois name"
        else:
            update_name(temp)
            assistant_details.name = temp
            return "Now you can call me "+ temp
    
    else:
        if answer == "":
            output("Don't know this one should i search on internet ?")
            ans = take_input()
            if "yes" in ans.lower():
                answer = check_on_wikipedia(query)
                if answer != "":
                    return answer
        
            else:
                output("can you please tell me what is it mean ?")
                ans = take_input()
                if 'it means' in ans:
                    ans = ans.replace('it means','')
                    
                    ans = ans.strip()
                    value = get_ans_from_memory(ans)

                    if value == "":
                        return "can't help with this one"
                    else:
                        insert_question_and_answer(query, value)
                        return "Thanks i will remember it for the next time"
                else:
                    return "can't help with this one"
            