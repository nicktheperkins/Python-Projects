class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    # Use the pass keyword when you don not want to add any other properties or methods to the class.
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.gradyear)

x = Student("Nick", "Perkins", 2018)
x.welcome()