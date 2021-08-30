# For loops and while loops video notes
i = 0
while i < 10:
    print("{} iteration through the loop.".format(i))
    i += 1


# While Loop Challenge

# Execute a while loop.
i = 0
while i < 6:
    print(i)
    i += 1

# Use the break statement within a while loop.
# With the break statement we can stop the loop even if the while condition is true
i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Use the continue statement within a while loop.
# With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Use the else statement within a while loop.
# With the else statement we can run a block of code once when the condition no longer is true
i = 0
while i < 6:
    print(i)
    i += 1
else:
    print("i is not longer less than 6")
