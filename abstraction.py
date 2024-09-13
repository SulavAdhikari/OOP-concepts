from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self):
        pass

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# Concrete Class: Car
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is starting ")

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")

# Concrete Class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, cc):
        super().__init__(brand, model, year)
        self.cc = cc

    def start_engine(self):
        print(f"The {self.brand} {self.model} engine is starting ")

    def display_info(self):
        super().display_info()
        print(f"Engine capacity: {self.cc}cc")

# Creating instances of the concrete classes
my_car = Car("Toyota", "supra", 2012, 2)
my_motorcycle = Motorcycle("Honda", "CBR", 2021, 599)

# Using methods from both the abstract class and the concrete classes
my_car.display_info()      # Inherited and extended method
my_car.start_engine()      # Implemented abstract method

print()  # Line break for readability

my_motorcycle.display_info()  # Inherited and extended method
my_motorcycle.start_engine()  # Implemented abstract method



class Bus(Vehicle):
    def test_method(self):
        print("test")

try:
    a = Bus("Tesla", "cybertruck", 2020) # Cannot instantiate abstract class without the abstract method.
    a.test_method()
    a.start_engine()
except TypeError as e:
    print(e)
