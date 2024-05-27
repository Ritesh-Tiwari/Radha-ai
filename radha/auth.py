from output_module import output
from database import login, getUser
def auth():
    output('Your User Name Please...')
    username = input ('Username : ')
    output('Your Password Please...')
    password = input ('Password : ')
    msg = login(username, password)
    if len(msg) ==0:
        output("Wrong username and password")
    else:
        output("Hello sir....")
  
# auth()

def changePassword():
    output('Your User Name Please...')
    username = input ('Username : ')
    data = getUser(username)
    if len(data)==0:
        output('User not found')
    else:
        output("Enter New Password...")
        new_pass = input("Enter new Password : ")
        output("Enter Confirm Password...")
        conf_pass = input("Enter new Password : ")
        while new_pass != conf_pass :
            output("Password does not match...")
            output("Please enter again...")            
            conf_pass = input("Enter new Password : ")
        
        
        
    # output('Your Password Please...')
    # password = input ('Password : ')
    # msg = login(username, password)
    # if len(msg) ==0:
    #     output("Wrong username and password")
    # else:
    #     output("Hello sir....")
  

changePassword()