

class Customer:

    def __init__(self, name, age, balance=0, is_vip = False) -> None:
        self.name = name
        self.balance = balance
        self.__age = age        
        self.is_vip = is_vip

    def __str__(self):
        return f"Customer {self.name}"        

    def deposit(self, balance):
        self.balance += balance

    def make_vip(self):
        self.is_vip = True
        return self.is_vip

    def remove_vip(self):
        self.is_vip = True

    def deduct_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False