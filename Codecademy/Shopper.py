class Shop:
    def __init__(self,Items,Stock,Workers):
        self.Items = Items
        self.Stock = Stock
        self.Workers = Workers
        self.out_of_stock = False
    def __repr__(self):
        return f" {self.Items} has a stock of {self.Stock} and is assigned to the worker {self.Workers}"
    
    def stockno(self):
        if self.Stock == 0:
            self.out_of_stock = True
        return f"{self.Items} has run out of stock.We are sorry for the inconvenience"

    def addstock(self,amount):
        if self.out_of_stock == True:
            self.Stock += amount
            return f"{self.Items} is back in Stock"
        else:
            self.Stock += amount

    def shelf_no(self,shelf_no):
        return f"{self.Items} is on the {shelf_no} assigned to the worker {self.Workers}"

class Shopper:
    def __init__(self,item,amount,name):
        self.item = item
        self.amount = amount
        self.name = name
    def __repr__(self):
        return f"The shopper {self.name} is here for {self.item} that he wants {self.amount} pieces of"

    def buy(self):
        if self.amount > self.item.Stock:
            return f"Sorry {self.name}, we only have {self.item.Stock} pieces of {self.item.Items} in stock."
        else:
            self.item.Stock -= self.amount
            return f"{self.name} has successfully purchased {self.amount} pieces of {self.item.Items}. Remaining stock: {self.item.Stock}"

    def ask(self):
        return f"{self.name} is asking for {self.amount} pieces of {self.item.Items}"

    def return_item(self):
        self.item.Stock += self.amount
        return f"{self.name} has returned {self.amount} pieces of {self.item.Items}. Updated stock: {self.item.Stock}"