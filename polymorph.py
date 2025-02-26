class cat:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print("Hey I am a cat. My name is",self.name,", I am",self.age,"years old.")
    def sound(self):
        print("I say Meow")

class dog:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print("Hey I am a dog. My name is",self.name,", I am",self.age,"years old.")
    def sound(self):
        print("I bark loudly")

class lion:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print("Hey I am a lion. My name is",self.name,", I am",self.age,"years old.")
    def sound(self):
        print("I roar scary")

o1=cat('Mini',2.5)
o1.info()
o1.sound()

o2=dog('Dodo',6)
o1.info()
o1.sound()

o3=lion('Kenz',9)
o1.info()
o1.sound()


for animal in(o2,o1,o3):
    animal.info()
    animal.sound()