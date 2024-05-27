import psycopg2
from psycopg2 import sql
from internet import check_internet_connection

def create_connection():
    # Connect to the PostgreSQL server
    connection = psycopg2.connect(database = "radha-ai", 
                        user = "avcdev", 
                        host= 'localhost',
                        password = "avc2019",
                        port = 5432)
    
    # connection = psycopg2.connect(database = "radha-ai", 
    #                     user = "avc", 
    #                     host= 'localhost',
    #                     password = "avcpass",
    #                     port = 5432)

    return connection

def getUser(username):
    con = create_connection()
    cur = con.cursor()
    cur.execute(f"select * from users where username='{username}'")
    return cur.fetchall()[0][1]

def getUserID(username):
    con = create_connection()
    cur = con.cursor()
    cur.execute(f"select * from users where username='{username}'")
    return cur.fetchall()[0][0]


def getLastLogin(username):
    con = create_connection()
    cur = con.cursor()
    cur.execute(f"select * from last_login where user_id ='{getUserID(username)}")
    return cur.fetchall()[0][2]


def updatePassword(username, password):
    
    con = create_connection()
    cur = con.cursor()
    
    query = "update users set password = '"+password+"' where username='"+username+"'"
    try:
        cur.execute(query)
        con.commit()
        
    except Exception as e:
        # Handle any database errors
        print(f"An error occurred: {e}")
        con.rollback()
    finally:
        # Ensure the connection is closed
        if con:
            con.close()

def login(username, password):
    con = create_connection()
    cur = con.cursor()
    cur.execute(f"select * from users where username='{username}' and password ='{password}'")

    return cur.fetchall()

def addNewUser(username,email, password):
    con = create_connection()
    cur = con.cursor()
    try:
        cur.execute(f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}')")
        con.commit()
    except Exception as e:
        # Handle any database errors
        print(f"An error occurred: {e}")
        con.rollback()

    finally:
        # Ensure the connection is closed
        if con:
            con.close()
    
def deleteUser(username):
    con = create_connection()
    cur = con.cursor()
    try:
        cur.execute(f"delete from users where username ='{username}")
        con.commit()
        
    except Exception as e:
        # Handle any database errors
        print(f"An error occurred: {e}")
        con.rollback()
    finally:
        # Ensure the connection is closed
        if con:
            con.close()


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

    try:
        # Insert new data
        query = "INSERT INTO qusandans VALUES('"+ question+"','"+ answer +"')"
        cur.execute(query)
        con.commit()
    except Exception as e:
        # Handle any database errors
        print(f"An error occurred: {e}")
        con.rollback()
    finally:
        # Ensure the connection is closed
        if con:
            con.close()
    
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
    

def insertSearchHistory(user_id, searchQuery):
    con = create_connection()
    cur = con.cursor()

    try:
        # Using parameterized query to prevent SQL injection
        query = f"INSERT INTO commands (user_id, command_text) VALUES ({user_id},'{searchQuery}')"
        cur.execute(query)
        
        # Commit the transaction
        con.commit()

       
    except Exception as e:
        # Handle any database errors
        print(f"An error occurred: {e}")
    finally:
        # Ensure the connection is closed
        if con:
            con.close()