from Self_use import *
from find_split_slice import *

p = greet.capitalize()
a = result.count()

class Car:
    wheels = 4
    steering = 1
    fuel1 = "diesel"
    fuel2 = "petrol"


    def __init__(self, mirror, seats, oil):
        self.mirror = mirror
        self.seats = seats
        self.oil = oil

    def available_car(self):

    
        if self.seats == 5:
            print("We have Hatch back, Sedan and Compact SUV")
            choices = input("Enter your choice: ")
            if self.y== 10:
                pass

            for choice in choices:
                print("We have Blue, Red and Black")
                choose= input("Enter your choice: ")

                if choose == "Blue":
                    print("Sorry! out of stock. We will notify you!")
                elif choose == "Red":
                    print("Sorry! out of stock. We will notify you!")
                else:
                    print("Chosen colour available")
                break
        else:
            print("We dont have that now")

                    
        if self.mirror == "rear view":
            print("ok")

        else:
            print("We dont have that")
        #return choose
                    
    def fuel_mode(self):

        fuel = input("Enter choice of fuel you want for your car: ")
        if fuel == "Petrol":
            print("Your choice of fuel ",Car.fuel2, "is available") 
        else:
            print("We dont have", Car.fuel1)

        if self.oil == "Indian oil":
            print("Your choice of oil is avilable")
        else:
            print("Sorry! we don't have that")

        
""" car_choice = Car("rear view", 5, "Indian oil")
car_choice.available_car()
car_choice.fuel_mode() """

class Tractor(Car):

    #When you add the __init__() function, the child class will no longer inherit 
    # the parent's __init__() function

    # The child's __init__() function overrides the inheritance of the parent's __init__() function

    #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
    #    def __init__(self, mirror, seats, oil):
    #    Car().__init__(self, seats, oil)
    
    # By using the super() function, you do not have to use the name of the parent element, 
    # it will automatically inherit the methods and properties from its parent.

    #tractor_polish should be a variable, and passed into the Tractor class when creating Tractor instances. 
    # To do so, add another parameter in the __init__() function and pass it in Tractor() calss
    #   while creating instance to it

    def __init__(self, mirror, seats, oil, polish):
        super().__init__(mirror, seats, oil)
        self.tractor_polish = polish

    def buy_tractor(self):
        self.seats = 4
        print("Yes we have", self.seats, "seats")

        if self.tractor_polish == "Silver":
            print("We have it")
        else:
            print("Sorry we dont have that")


tractor = Tractor("rear view", 5, "Indian oil" , "Silver")
tractor.buy_tractor()




            


