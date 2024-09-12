# Parent Class
class Vehicle:
    def __init__(self, name, color, topspeed):
        self.name = name
        self.color = color
        self.topspeed = topspeed

    def display_info(self):
        print(f"name: {self.name}, color: {self.color}, topspeed: {self.topspeed}")

    def start_engine(self):
        print("The engine is starting...")

# Child Class
class Car(Vehicle):
    def __init__(self, name, color, topspeed, doors):
        # Calling the parent class's constructor
        super().__init__(name, color, topspeed)
        self.doors = doors

    # Overriding the display_info 
    def display_info(self):
        super().display_info()  # Call the parent class's display_info method
        print(f"Doors: {self.doors}")

    def honk(self):
        print("Honk! Honk!")


greentoyota = Car("Toyota", "gren", 180, 2)



greentoyota.display_info()

greentoyota.start_engine()

greentoyota.honk()          