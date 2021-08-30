# For loops and while loops video notes
i = 0
for i in range(10):
    print("{} iteration through the loop.".format(i))
    i += 1 #i = i + 1


# For Loop Challenge

# Execute a for loop.
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

# Use the break statement within a for loop.
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

# Use the continue statement within a for loop.
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# Use the range() function within a for loop.
# The range() function will loop through a set of code a specified number of times.
# range(2, 30, 3) This means increment the sequence by 3's from 2 to 30 (but not incliding 30)
for x in range(6):
    print(x)

# Use the else keyword within a for loop.
for x in range(6):
    print(x)
else:
    print("Finally finished!")
