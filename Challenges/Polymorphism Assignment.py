class User:
    # Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0
    
    # Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("The password or email is incorrect.")

# Child class with two of its own attributes
class Employee(User):
    base_pay = 11.00
    department = 'General'
    pin_number = '3980'
    
    def login(self):
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}".format(self.name))
        else:
            print("The pin or email is incorrect.")

# Child class with two of its own attributes
class Customer(User):
    mailing_address = ' '
    mailing_zipcode = '84003'
    mailing_list = True
    
    def login(self):
        entry_email = input("Enter your email: ")
        entry_zip = input("Enter your zipcode: ")
        if (entry_email == self.email and entry_zip == self.mailing_zipcode):
            print("Welcome back, {}".format(self.name))
        else:
            print("The zipcode or email is incorrect.")