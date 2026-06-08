import json
def user_task_details(task,times):
    try:
        with open("task_list.json", "r") as file:
            todo= json.load(file)

    except Exception:
        todo = {}
  
    todo[task]=times
    with open("task_list.json", "w") as file:
            json.dump(todo, file, indent=4)
  








       