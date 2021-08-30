
import os


fName = 'Hello.txt'

fPath = 'C:\\Users\\Nick\\Downloads\\Python Projects\\Modules Practice\\A\\'


abPath = os.path.join(fPath, fName) # This creates and absolute file path after joining our two variables above.
print(abPath)
