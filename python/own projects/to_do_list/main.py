from no_task_page import no_task
from new_task_page import output
from task_sheduler import user_task_details
from time_setter import alarm
from delete_task import delete_tasK

import json
import time




while True:
    


    try:
        with open("task_list.json", "r") as file:
            todo = json.load(file)

    except Exception:
        todo = {}
    if not todo:
        
        no_task()
        time.sleep(1)
        

    else:
        print("Available tasks\n")
        time.sleep(1)

        for key, value in todo.items():
            print(key, value)
            print()
            time.sleep(1)
    
    new_task = input(
        "Enter N for new task creation \n T for show all list \n Enter A to continue \n D to delete old entries:"
    )

    
    
    

    if new_task.upper() == "N":

        task, times = output()

        last_action = time.time()

        user_task_details(task, times)
    elif new_task.upper()=="A":
        alarm()
    elif new_task.upper()=="D":
              delete_tasK()
                    
            
                
    elif new_task.upper()=="T":
        for key, value in todo.items():
            print(key, value)
    else:

        for key, value in todo.items():
            print(key, value)
            alarm()