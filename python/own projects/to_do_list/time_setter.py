import time 
import datetime
import pygame
import json
import keyboard

def alarm():
    is_running=True
    sound_file="x.mp3"
    with open("task_list.json", "r") as file:
            todo = json.load(file)
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if keyboard.is_pressed("space"):
                    break
            
        
        
        for key,value in todo.items():
            if value == current_time:
                
                print(key)
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    user_pressed_next=input("space to stop")
                    if user_pressed_next=="" or user_pressed_next==" ":
                        pygame.mixer.music.stop()
                        break
                    time.sleep(1)
                is_running=False
        time.sleep(1)
            
            
            
            
