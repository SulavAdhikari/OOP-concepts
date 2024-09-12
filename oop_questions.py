# Encapsulation 
class car:
    def __init__(self):
        # encapsulated
        self.__current_speed = 0  # encapsulating by adding __ before the name of the variable

    # encapsulated
    def __increase_speed(self, speed): # encapsulating by addind __ before the name of the method       
        self.__current_speed = self.__current_speed + speed 

    # encapsulated
    def __decrease_speed(self, speed): # encapsulating by addind __ before the name of the method
        self.__current_speed = self.__current_speed - speed

    def get_current_speed(self):
        return self.__current_speed
    
    def accelerate(self, speed):
        self.__increase_speed(speed)
        print("now moving at the speed of: " + str(self.__current_speed))

    def decelerate(self, speed):
        self.__decrease_speed(speed)
        print("now moving at the speed of: " + str(self.__current_speed))

print("\n\nBeggining of Encapsulation:")
mustang_gt = car()

try:
    print(mustang_gt.__current_speed)  
except AttributeError:
    print("The variable current_speed has been set up to be encapsulated")

try:
    mustang_gt.__increase_speed(10)
except AttributeError:
    print("The method increase_speed has been set up to be encapsulated")

try:
    mustang_gt.__decrease_speed(10)
except AttributeError:
    print("The method decrease_speed has been set up to be encapsulated")


# printing current speed

print(mustang_gt.get_current_speed())
mustang_gt.accelerate(10)
print(mustang_gt.get_current_speed())
mustang_gt.decelerate(10)
print(mustang_gt.get_current_speed())


# Inheritence