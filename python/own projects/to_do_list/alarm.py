import time 
import datetime
import pygame

x=input("Enter the task:")
time_inp=input("Ente time in HH:MM:SS format:")
print(f"Alarm set for {time_inp}")
sound_file="x.mp3"
is_running=True
while is_running:
    current_time=datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    if current_time==time_inp:
        print("WAKE up")
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
            
    is_running=False
    time.sleep(1)