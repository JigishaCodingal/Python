class computer:
    def __init__(self):
        self.aprice=800
        self.__sprice=1000#private data member
    def sell(self):
        print("The actual price of computer is",self.aprice)
        print("The selling price of computer is",self.__sprice)
    def change(self, a, s):
        self.aprice=a
        self.__sprice=s

c=computer()#constructor will be called
c.sell()

c.aprice=1000
c.__sprice=1400 #__sprice not accessible
c.sell()

c.change(2000,2400)
c.sell()


