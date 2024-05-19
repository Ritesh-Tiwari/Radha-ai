import psycopg2
from psycopg2 import sql
from internet import check_internet_connection

def create_connection():
    # Connect to the PostgreSQL server
    # connection = psycopg2.connect(database = "radha-ai", 
    #                     user = "avcdev", 
    #                     host= 'localhost',
    #                     password = "avc2019",
    #                     port = 5432)
    
    connection = psycopg2.connect(database = "radha-ai", 
                        user = "avc", 
                        host= 'localhost',
                        password = "avcpass",
                        port = 5432)

    return connection
    
def get_questions_and_answers():
    con = create_connection()
    cur = con.cursor()
    cur.execute("select * from qusandans")
    return cur.fetchall()


def get_ans_from_memory(qus):
    rows = get_questions_and_answers()
    answer = ""

    for row in rows:
        if row[0].lower() in qus.lower():
           answer = row[1]
           break
    return answer


def insert_question_and_answer(question, answer):
    con = create_connection()
    cur = con.cursor()

    # Insert new data
    query = "INSERT INTO qusandans VALUES('"+ question+"','"+ answer +"')"
    cur.execute(query)
    con.commit()
        
# print(get_ans_from_memory("name"))  
insert_question_and_answer("pause music",'pause music')

def get_name():
    con = create_connection()
    cur = con.cursor()

    # Get assistant name
    query = "select value from memory where name ='assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]


def update_name(new_name):
    con = create_connection()
    cur = con.cursor()

    # Get assistant name
    query = "update memory set value = '"+new_name+"' where name='assistant_name'"
    cur.execute(query)
    con.commit()
    
# update_name("ram")
# print(get_name())

def updates_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()

    # Get assistant name
    query = "update memory set value = '"+str(last_seen_date)+"' where name='last_seen_date'"
    cur.execute(query)
    con.commit()


def get_last_seen():
    con = create_connection()
    cur = con.cursor()

    # Get assistant name
    query = "select value from memory where name ='last_seen_date'"
    cur.execute(query)
    return str(cur.fetchall()[0][0])
    


def turn_on_speech():
    if (check_internet_connection()):
        con = create_connection()
        cur = con.cursor()
        query = "update memory set value = 'on' where name='speech'"
        cur.execute(query)
        con.commit()
        return "okay i will speak now"
    else:
        return "Hey please turn on internet first"
    

def turn_off_speech():
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value = 'off' where name='speech'"
    cur.execute(query)
    con.commit()
    return "okay i won't speak"
    

def speak_is_on():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name='speech'"
    cur.execute(query)
    ans = str(cur.fetchall()[0][0])

    if ans == "on":
        return True
    else:
        return False