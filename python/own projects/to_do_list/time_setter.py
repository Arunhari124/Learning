import time 
import datetime
import pygame
import json

def alarm():
    is_running=True
    sound_file="x.mp3"
    with open("task_list.json", "r") as file:
            todo = json.load(file)
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        for key,value in todo.items():
            if value == current_time:
                print(key)
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
                is_running=False
        time.sleep(1)
            
            
            
            
