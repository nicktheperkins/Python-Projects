# In Python, the string data type can also be a tuple (an immutable list).
# In this case, each of the characters within the string would represent one immutable element.
name = 'Python'
print(len(name))

# “Enumerate” literally means to “determine the number of.”
# It can also mean to mention things one by one.
# The following will iterate through all of the elements with the string array.
for i in enumerate(name):
    print(i)
