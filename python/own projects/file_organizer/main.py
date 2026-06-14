import os 
import shutil
folder="c:/Users/Admin/Downloads"

for file in os.listdir(folder):
    path=os.path.join(folder,file)
    
    if os.path.isfile(path):
        ext =os.path.splitext(file)[1]
        if ext == ".mp4":
            os.makedirs("Videos", exist_ok=True)
            shutil.move(path, os.path.join("Videos", file))
        elif ext == ".exe":
            os.makedirs("software", exist_ok=True)
            shutil.move(path, os.path.join("software", file))
     