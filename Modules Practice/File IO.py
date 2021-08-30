# print(dir(str))
# print(help(str))

# I created a folder in my c drive titled python_projects
# In that folder I added a test.txt file

import os


# print(os.getcwd()) # prints the working directory


def writeData():
    data = '\nHello world!'
    with open('test.txt', 'a') as f: # 'a' append
        f.write(data)
        f.close()


def openFile():
    # print(help(open))
    with open('test.txt', 'r') as f: # 'r' read
        data = f.read()
        print(data)
        f.close()


if __name__ == "__main__":
    writeData()
    openFile()
