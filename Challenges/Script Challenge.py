
import os
import time


fPath = 'C:\\Users\\Nick\\Documents\\GitHub\\Python-Projects\\Modules Practice\\Script_Assignment_Directory\\'

def loop():
    for txt in os.listdir(fPath): #creates an array of files from the path
        if txt.endswith('.txt'):
            mod_time = os.path.getmtime(fPath + txt) #gets the time of last modification since the epoch
            local_time = time.ctime(mod_time) #converts the time in seconds since epoch to local time
            print(txt + " " + local_time)

loop()
