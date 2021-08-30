# Format() Function
# In Python, the format() function can do more than just string formatting.
    # It can convert a value into a specific data type format.
    # It can also format values to binary or even a float.
# The format() function takes two parameters: the values that need to be formatted and format specification (format_spec).
x = format(8, 'b')
print(x)

# In this code, we have addigned the variable c to the value of 8 to be formatted in binary by using the 'b' type.
    # Therefore, when it's printed, it gives the new binary format of 1000.

# Here is an example of string format concatenation while also formatting a value to different data types.
print("binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}".format(4))


# Format Challenge
# Execute a format() function.
x = format(0.5, '%')
print(x)
