class cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print("My name is",self.name,", I am",self.age,"years old.")
    def sound(self):
        print("I say Meow")

class dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print("My name is",self.name,", I am",self.age,"years old.")
    def sound(self):
        print("I bark")

o1=cat("Mini",2)#__init__
o2=dog("Dodo",7)#__init__

for animal in(o1,o2):
    animal.info()
    animal.sound()

