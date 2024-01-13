class Car:
    wheels = 4
    steering = 1
    fuel1 = "diesel"
    fuel2 = "petrol"
    x= 3


    def available_car(self, mirror, seats):

        self.mirror = mirror
        self.seats = seats
        height =1
        if seats == 5:
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

                    
        if mirror == "rear view":
            print("ok")

        else:
            print("We dont have that")
        return choose
                    
    def fuel_mode(self):
        fuel = input("Enter choice of fuel you want for your car: ")
        if fuel == "Petrol":
            print("Your choice of fuel is ", Car.fuel2, "is available") 
        

        else:
            print("We dont have", Car.fuel1)
    # since we used self object, the scope of the variable is available to all methods
    # since height was not given self as object name, the scope of height is within that method alone
"""         if self.mirror== 0:
            print(height) """

        
# if yhere is no initiater there no need to pass arguments while creating instance to class.
car_choice = Car()
car_choice.available_car("rear view",5)
car_choice.fuel_mode()

# in python, the object is passed as first argument to the method, so we use self as object
Car.available_car("yes",5)

# to change the global var value, we can use classname.var name = valuer you want
Car.x = 5

#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")








            


