#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuples are unchangeable, or immutable.
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#The del keyword can delete the tuple completely:
this_tuple = ("apple", "banana", "cherry")
del this_tuple
#print(this_tuple) #this will raise an error because the tuple no longer exists

#----------------------------------UNPACKING TUPLE-----------------------------------
print("UNPACKING TUPLE")
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print("UNACKING DONE")
#The number of variables must match the number of values in the tuple, 
# if not, you must use an asterix to collect the remaining values as a list.

#If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) #apple
print(yellow) #banana
print(red)  #['cherry', 'strawberry', 'raspberry']

#If the asterix is added to another variable name than the last, 
#Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)  #apple
print(tropic) #['mango', 'papaya', 'pineapple']
print(red)    #cherry

"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""