import threading
import time


def walk_dog(first,last):
    time.sleep(5)
    print(f"YOu finished walking the dog {first} {last} ")
    
    
def take_out_trash():
    time.sleep(2)
    print("you take out the trash")

def mail_get():
    time.sleep(3)
    print("mail mail")
    
    


chore1=threading.Thread(target=walk_dog,args=("nigga","gay"))
chore1.start()
chore2=threading.Thread(target=take_out_trash)
chore2.start()
chore3=threading.Thread(target=mail_get)
chore3.start()


chore1.join()
chore2.join()
chore3.join()

print("ALl chores are complete ")