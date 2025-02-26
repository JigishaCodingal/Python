class parrot:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def sing(self,song):
        print("I sing",song)
    def dance(self):
        print("I love to dance with singing")
    def intro(self):
        print("My name is",self.name,"of age",self.age)
o1=parrot("Mitu",2)
o1.intro()
o1.sing("Hurrey")
o1.dance()
o2=parrot("Nonu",2.5)
o2.intro()
o2.sing("Happy")
o2.dance()