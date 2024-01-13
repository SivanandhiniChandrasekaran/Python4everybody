class Pizza:

    def __init__(self, size, extras):
        self.size = size
        self.extras = extras

    def preparation(self):
        if self.size == "large":
            print("Yes we have")

    def toppings(self):
        if self.extras == "cheese":
            print("double cheese aadded")

class Food(Pizza):

    def __init__(self, size, extras,foodType):
        super().__init__(size, extras)
        self.foodType = foodType


    def cuisine(self):
        if self.foodType == "Italian":
            print("we have pizza.")
            

    def order(self):
        if self.size == "small":
            print("yes. ok")

orders = Food("large","cheese","Italian")
orders.preparation()
orders.toppings()
orders.order()
