class Computer:

    def __init__(self,a,b):
        self.__maxprice =a #private : not accessible outside the class
        self.price=b #public : can be accessible

    def sell(self):
        print("Selling Price: ",self.__maxprice)
        print("Actual Price: ",self.price)

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer(1000,800)
c.sell()

# change the price
c.maxprice = 2000
c.price=1000
c.sell()

# using setter function
c.setMaxPrice(2000)
c.sell()

