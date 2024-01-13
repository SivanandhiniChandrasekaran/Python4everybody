
class StaticMethod:
    food = "pizza"

    @staticmethod
    def static_method():
        size = "Hi"
        print(size)

StaticMethod.static_method()

# Both the below print statements are valid but using format() is the appropriate way        
print("we have", 5, "of that and 24 of this")
print("we have {} of that and {} of this".format(5, 24))
      








    

