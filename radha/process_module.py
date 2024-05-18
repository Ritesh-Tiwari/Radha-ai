from output_module import output
from time_module import get_time
from database import get_ans_from_memory, insert_question_and_answer
from input_module import take_input
from internet import check_internet_connection, check_on_wikipedia

def process(query):
    answer = get_ans_from_memory(query)

    if answer == "":
        answer = check_on_wikipedia(query)
        if answer != "":
            return answer

    elif "the time" in query:
        return "Time is " + get_time()
    
    elif answer == "Radha":
        return "i am " + answer
    
    elif answer == "check internet connection":
    
        if check_internet_connection():
            return "internet is connected."
        else :
            return "internet is not connected"
    
    else:
        output("I don't know this one, can you please tell me what is it mean")
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
        