#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is ordered* and changeable. No duplicate members.

#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']
print(thislist[1])

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:3] = ["blackcurrant", "watermelon"]
print(thislist1)

#Change the second value by replacing it with two new values:
thislist2 = ["apple", "banana", "cherry"]
thislist2[1:2] = ["blackcurrant", "watermelon"]
print(thislist2)

#Insert "watermelon" as the third item:
thislist3 = ["apple", "banana", "cherry"]
thislist3.insert(2, "watermelon")
print(thislist3)

#Using the append() method to append an item:
thislist4 = ["apple", "banana", "cherry"]
thislist4.append("orange")
print(thislist4)

#To append elements from another list to the current list, use the extend() method.
thislist5 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist5.extend(tropical)
print(thislist5)

#The extend() method does not have to append lists, you can add any iterable 
# object (tuples, sets, dictionaries etc.). and output will be a list of all 
# elements in list and tuple together
thislist6 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist6.extend(thistuple)
print(thislist6)

#-----------DELETING ITEMS IN A LIST------------------------------

#The remove() method removes the specified item.
thislist7 = ["apple", "banana", "cherry"]
thislist7.remove("banana")
print(thislist7)

#The pop() method removes the specified index.
thislist8 = ["apple", "banana", "cherry"]
thislist8.pop(1)
print(thislist8)
#If you do not specify the index, the pop() method removes the last item
thislist8.pop()
print(thislist8)

#The del keyword also removes the specified index:
thislist9 = ["apple", "banana", "cherry"]
del thislist9[0]
print(thislist9)

#The del keyword can also delete the list completely.
thislist10 = ["apple", "banana", "cherry"]
del thislist10
#print(thislist10) #this will cause an error because you have succsesfully deleted "thislist10".

#The clear() method empties the list.
thislist11 = ["apple", "banana", "cherry"]
thislist11.clear()
print(thislist11)

#------------------------------------SORTING LISTS------------------------------------------

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#By default the sort() method is case sensitive, resulting in all capital letters being sorted 
# before lower case letters:
print("HELLO")
thislist12 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist12.sort()
print(thislist12)
thislist12.sort(reverse = True)
print(thislist12)



#To sort descending, use the keyword argument reverse = True:
print("YEAH")
thislist13 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist13.sort(reverse = True)
print(thislist13)

#Perform a case-insensitive sort of the list :
thislist14 = ["banana", "Orange", "Kiwi", "cherry"]
thislist14.sort(key = str.lower)
print(thislist14)

#Reverse the order of the list items:
thislist15 = ["banana", "Orange", "Kiwi", "cherry"]
thislist15.reverse()
print(thislist15)

#------------------------------------COPY LIST---------------------------------------------------------

#Make a copy of a list with the copy() method:
this_list = ["apple", "banana", "cherry"]
my_list = this_list.copy()
print(my_list)

#Another way to make a copy is to use the built-in method list()
thislst = ["apple", "banana", "cherry"]
mylst = list(thislst)
print(mylst)

#------------------------------------JOIN LIST-----------------------------------------------------------------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Append list2 into list1:
list_1 = ["a", "b" , "c"]
list_2 = [1, 2, 3]

for x in list_2:
  list_1.append(x)

print(list_1)

#Use the extend() method to add list2 at the end of list1:
listA = ["a", "b" , "c"]
listB = [1, 2, 3]

listA.extend(listB)
print(listA)

#if you multiply a list with a number, it multiplies and prints
a = ["given", "when", "then"]
print(a*2) #['given', 'when', 'then', 'given', 'when', 'then']


"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""