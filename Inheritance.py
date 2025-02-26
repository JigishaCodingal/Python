class person():
    def __init__(self,n,a):#constructor
        self.name=n
        self.age=a
    def disp(self):
        print('My name is',self.name,', I am',self.age,'years old.')

class emp(person):#emp is child class of person
    def __init__(self,n,a,s,d):#constructor of emp
        self.salary=s
        self.desig=d
        person.__init__(self,n,a)#super() : parent
    def show(self):
        self.disp()#parent class function
        print('I am working as a ',self.desig,'and getting',self.salary)
o1=emp('Frozy',37,4800,'Clerk')
o1.show()



