# The lambda keyword is used as an anonymous function.
# An anonymous function is a single-line function that has no name
    # that can have any number of arguments, but only one expression.
    # It is similar to a regular function, but is used for a shorter
    # amount of time and is used when we want to pass another function
    # in as an argument.

def multiply(i):
    return i * i;

y = lambda x: x * x * x

print(y(20))
print(multiply(3))

# Lambda Challenge
# Create a lambda function.
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
