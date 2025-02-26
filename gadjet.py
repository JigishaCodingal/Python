class gadget:
    def __init__(self, n, m):
        self.name=n
        self.model=m
    def disp(self):
        print("It's a ",self.name,", model:",self.model)

class mobile(gadget):
    def __init__(self,n,m,c,p):
        self.cmpy=c
        self.price=p
        gadget.__init__(self,n,m)
    def show(self):
        self.disp()
        print("It is manufactured by",self.cmpy," and its cost is",self.price)

o1=mobile("Mobile Phone","16 Pro","Apple",160000)
o1.show()
