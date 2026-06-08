from no_task_page import no_task
from new_task_page import output
from task_sheduler import user_task_details
from time_setter import alarm

import json
import time
import threading

last_action = time.time()
alarm_triggered=False


def idle_checker():
    global last_action, alarm_triggered

    while True:
        if not alarm_triggered and time.time() - last_action >= 10:
            alarm_triggered = True
            alarm()
            

        time.sleep(1)


threading.Thread(target=idle_checker, daemon=True).start()


while True:

    try:
        with open("task_list.json", "r") as file:
            todo = json.load(file)

    except Exception:
        todo = {}

    if not todo:
        no_task()

    else:
        print("Available tasks\n")

        for key, value in todo.items():
            print(key, value)
            print()

    new_task = input(
        "Enter N for new task creation or T for show all list: "
    )

    last_action = time.time()

    if new_task.upper() == "N":

        task, times = output()

        last_action = time.time()

        user_task_details(task, times)

    else:

        for key, value in todo.items():
            print(key, value)