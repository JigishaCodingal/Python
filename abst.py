from abc import ABC,abstractmethod
class Animal(ABC):#polygon
    def behave(self):#area
        pass
class human(Animal):#square
    def behave(self,l):#area
        a=l*l
        print("Area=",a)
class snake(Animal):
    def behave(self):
        print("I can crawl and bite")
class dog(Animal):
    def behave(self):
        print("I can bark and jump")
class lion(Animal):
    def behave(self):
        print("I can roar and attack")

o1=human()
o1.behave(3)

o1=snake()
o1.behave()

o1=dog()
o1.behave()

o1=lion()
o1.behave()