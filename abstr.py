#abstraction
from abc import ABC, abstractmethod
class animal(ABC):#abstract class
    def behave(self):
        pass#nothing is happening

class human(animal):
    def behave(self):#has to recreate function
        print("I can walk and run")

class snake(animal):
    def behave(self):
        print("I can crawl")

class dog(animal):
    def behave(self):
        print("I can smell and bark")
        
class lion(animal):
    def behave(self):
        print("I can roar and attack")

o1=human()
o1.behave()

o1=snake()
o1.behave()

o1=dog()
o1.behave()

o1=lion()
o1.behave()

