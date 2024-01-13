
class VarCheck:
    food = "pizza"


    def global_var():
    # by defing a variable as global, we can use that even outside the method
        global size
        size = "Hi"
        print(size)

var = VarCheck
var.global_var()

# size variable was defined global. so no need instance to call it
print(size)
print(VarCheck.pizza)




    

