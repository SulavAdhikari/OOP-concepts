
class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, amount):
        self.stock -= 1

    def add_stock(self, amount):
        self.stock += amount

class Purchase:
    def __init__(self, product, customer, amount):
        self.customer = customer
        self.product = product
        self.amount = amount
        self.total_price = self.product.price * amount

    def __check_stock(self):
        if self.product.stock >= self.amount:
            return True
        raise ValueError("Insufficient stock for the product")
    
    def __check_balance(self):
        if self.customer.balance >= self.total_price:
            return True
        raise ValueError("Please Check your balance")
    
    def is_valid(self):
        if self.__check_balance() and self.__check_stock():
            return True
        return False
    
    def confirm(self):
        if self.is_valid():
            self.customer.deduct_balance(self.total_price)
            self.product.sell(self.amount)
            return True
        return False