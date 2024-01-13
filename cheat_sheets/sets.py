#Once a set is created, you cannot change its items, but you can add new items.
#A set is a collection which is both unordered and unindexed. No duplicate members.
#You cannot access items in a set by referring to an index or a key, since they are unorderd & unindexed

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicate values will be ignored:
this_set = {"apple", "banana", "cherry", "apple"}
print(this_set)

#Add an item to a set, using the add() method:
thisset1 = {"apple", "banana", "cherry"}
thisset1.add("orange")
print(thisset1)

#To add items from another set into the current set, use the update() method.
thisset2 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset2.update(mylist)
print(thisset2)

#To remove an item in a set, use the remove(), or the discard() method.
thisset3 = {"apple", "banana", "cherry"}
thisset3.remove("banana")
print(thisset3)
#If the item to remove does not exist, remove() will raise an error

thisset4 = {"apple", "banana", "cherry"}
thisset4.discard("banana")
print(thisset4)
#If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, but this method will remove the last item. 
# Remember that sets are unordered, so you will not know what item that gets removed.
#The return value of the pop() method is the removed item.
#Remove the last item by using the pop() method:
print("SETS")
thisset5 = {"apple", "banana", "cherry"}
x = thisset5.pop()
print(x)
print(thisset5)

#The clear() method empties the set:
thisset6 = {"apple", "banana", "cherry"}
thisset6.clear()
print(thisset6)

#The del keyword will delete the set completely:
thisset7 = {"apple", "banana", "cherry"}
del thisset7
#print(thisset7)

#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:
set_1 = {"a", "b" , "c"}
set_2 = {1, 2, 3}
set_1.update(set_2)
print(set_1)

#Both union() and update() will exclude any duplicate items.
#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
z1 = x1.intersection(y1)
print(z1)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
x2.symmetric_difference_update(y2)
print(x2)

#The symmetric_difference() method will return a new set, 
# that contains only the elements that are NOT present in both sets
x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}
z3 = x3.symmetric_difference(y3)
print(z3)

"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""