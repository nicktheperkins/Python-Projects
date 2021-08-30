class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduction(self):
        print("Hello my name is " + self.name)

p = Person("Nick", 26)
p.introduction()