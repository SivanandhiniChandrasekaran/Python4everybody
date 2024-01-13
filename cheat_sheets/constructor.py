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
        
#If there is an initiater, then the arguments needed to be passed to the class
#  while creating an instancefor the class

#The arguments passed in class are common for both methods here. We are passing all the arguments needed 
#   for available_car and fuel_mode method in while creating class instance as the __init__ has them
car_choice = Car("rear view", 5, "Indian oil")
car_choice.available_car()
car_choice.fuel_mode()





            


