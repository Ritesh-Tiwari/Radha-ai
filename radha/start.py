from input_module import take_input
from process_module import process
from output_module import output
from welcome import greet
from database import login
import os

os.system("clear")
login()
# Welcome message
greet()


while(True):
    i = take_input()
    o = process (i)
    if o == "ignore":
        print ("ignoring....\n")
    else:
        output(o)



