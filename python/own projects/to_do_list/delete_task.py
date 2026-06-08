# Initial dictionary
import json
def delete_tasK():
        try:
                with open("task_list.json", "r") as file:
                        todo = json.load(file)

        except Exception:
                todo = {}
        
        
        print(todo)

# Take key input from the user
        key_to_delete = input("Enter the key you want to delete: ")

# Safely remove the key and its value
        todo.pop(key_to_delete, None)
        with open("task_list.json", "w") as file:
            json.dump(todo, file, indent=4)

        print("avalilebl task", todo)

