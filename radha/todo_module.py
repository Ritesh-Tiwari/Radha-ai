from database import create_connection
from output_module import output
import datetime

class TodoMoudle():
    # todo : 
    # 1 . add new task
    # 2 . get all task
    # 3 . search a task (id, name. due_date, status)
    # 3 . update task using id, name, due_date, status 
    #
    # function name :
    # get_all_todo()
    # add_todo()
    # search_todo_id(id)
    # search_todo_name(name)
    # search_due_date(due_date)
    # search_status(status)
    # update_task_name(name)
    # update_due_date(due_date)
    # update_status(status)

    def get_all_todo():
        
        conn = create_connection()
        cur =conn.cursor()
        cur.execute("select * from todo_list")

        return cur.fetchall()
        
    def todayTodo():
        conn = create_connection()
        cur =conn.cursor()
        cur.execute("select * from todo_list where due_date ='"+str(datetime.datetime.now().date())+"'")
        return cur.fetchall()
    
    def tomorrowTodo():
        conn = create_connection()
        cur =conn.cursor()
        next_day = datetime.datetime.now().date() + datetime.timedelta(days=1)
        cur.execute("select * from todo_list where due_date ='"+str(next_day)+"'")
        return cur.fetchall()
   
    def dueTodo():
        conn = create_connection()
        cur =conn.cursor()
        yesterday = datetime.datetime.now().date() - datetime.timedelta(days=1)
        cur.execute("select * from todo_list where due_date ='"+str(yesterday)+"'")
        return cur.fetchall() 
        
    def addTodo():
        output("Enter Task Name...")
        task_name = str(input("Name of the Task : "))
        output("Enter due date... ")
        due_date = str(input('Due Date (yyyy-mm-dd) : '))
        output("status...")
        status = str(input("Status : "))
        con = create_connection()
        cur = con.cursor()

        # Insert new data
        query = "INSERT INTO todo_list (task, due_date, status) VALUES('"+task_name+"','"+ due_date +"','"+ status +"')"
        cur.execute(query)
        con.commit()
        return "New task added "

    def deleteTodo():
        todos = TodoMoudle.get_all_todo()
        for i in todos:
            print( f"\nID. {i[0]}, {i[1]}, due date {i[2]} and status {i[3]}")
        output("Which task do you want to delete ? ")
        tod_id = input("Task No. : ")
        con = create_connection()
        cur = con.cursor()
        query = "delete from todo_list where id = "+ tod_id
        cur.execute(query)
        con.commit()
        return "Task Deleted. Sir"


# a = TodoMoudle.get_all_todo()
# for i in a:
#     output(f"No. {i[0]}, {i[1]}, due date is {i[2]} and status {i[3]}")
# print(TodoMoudle.tomorrowTodo())