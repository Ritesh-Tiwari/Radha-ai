import psycopg2
from psycopg2 import sql

def create_connection():
    # Connect to the PostgreSQL server
    connection = psycopg2.connect(database = "radha-ai", 
                        user = "avcdev", 
                        host= 'localhost',
                        password = "avc2019",
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
# insert_question_and_answer("check internet connection",'check internet connection')