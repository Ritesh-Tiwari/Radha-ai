from database import create_connection
from output_module import output

# from output_module import output
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

class TodoMoudle():
    def get_all_todo():
        
        conn = create_connection()
        cur =conn.cursor()
        cur.execute("select * from todo_list")

        return cur.fetchall()
        
    def addTodo():
        print("Enter Task Name :")
        task_name = str(input())
        print("Enter due date (yyyy-mm-dd) ")
        due_date = str(input())
        print("status :")
        status = str(input())
        con = create_connection()
        cur = con.cursor()

        # Insert new data
        query = "INSERT INTO todo_list (task, due_date, status) VALUES('"+task_name+"','"+ due_date +"','"+ status +"')"
        cur.execute(query)
        con.commit()
        print ("New task added ")

# a = TodoMoudle.get_all_todo()
# for i in a:
#     output(f"No. {i[0]}, {i[1]}, due date is {i[2]} and status {i[3]}")
