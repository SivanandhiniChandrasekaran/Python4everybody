#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Get the value of the "model" key:
thisdict1= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# both are valid and same. just diff ways to get value in dict
x = thisdict1["model"]
x = thisdict1.get("model")

#Get a list of the keys:
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
y = thisdict2.keys()
print("hiiii", y)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

#Add a new item to the original dictionary, and see that the keys list gets updated as well:
z = car.keys()
print(z) #before the change
car["color"] = "white"
print(z) #after the change

#Make a change in the original dictionary, and see that the values list gets updated as well:
bus = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
ab = bus.values()
print(ab) #before the change
bus["year"] = 2020
print(ab) #after the change


#The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)

#The update() method will update the dictionary with the items from the given argument.
thisdiction = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdiction.update({"year": 2020})

#The pop() method removes the item with the specified key name:
thisdictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictionary.pop("model")
print(thisdictionary)

#The popitem() method removes the last inserted item 
# (in versions before 3.7, a random item is removed instead):
thisdictiona = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964  
}
thisdictiona.popitem()
print(thisdictiona)

#The del keyword removes the item with the specified key name:
thedict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thedict["model"]
print(thedict)

#The del keyword can also delete the dictionary completely:
thisdicts = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdicts
#print(thisdicts) #this will cause an error because "thisdict" no longer exists.

#Print all key names in the dictionary, one by one:
thdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for wen in thdict:
  print(wen)
#Primt all the values one by one
for ren in thdict:
  print(thdict[ren])

#another way to print values
for tw in thdict.values():
  print(tw)

#another way to print keys
for gt in thdict.keys():
  print(gt)

#Loop through keys and values
for we, rt in thdict.items():
  print(we, rt)

"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
