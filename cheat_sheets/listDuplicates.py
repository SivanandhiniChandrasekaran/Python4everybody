
   
fhand = input("Enter a list:")
print(fhand)
elements = fhand.split()
print(elements)

new_list = []
for element in elements:
    if element not in new_list:
        new_list.append(element)
print(new_list)

#below are the mways to convert list to str
newstring = ''.join(new_list)
print(newstring)

newstr = ""
for x in new_list:
    newstr += x
print(newstr)


#convert list to dict as dict wont allow duplicated and convert it back to list

# result = dict.fromkeys(elements)
# print(result)
# end_result = list(result)
# print(end_result)

#adding 2 lists of same lenth into a dict
l1=[1,2,3,4]
l2=['a','b','c','d']
d1=zip(l1,l2)
print (d1)#Output:<zip object at 0x01149528>
#Converting zip object to dict using dict() contructor.
print (dict(d1))
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

#using enumerate
# enumerate(iterable, start=0)

# Parameters:
# Iterable: any object that supports iteration
# Start: the index value from which the counter is 
#               to be started, by default it is 0

l1=['a','b','c','d']
d1=dict(enumerate(l1))
print (d1)#Output:{0: 'a', 1: 'b', 2: 'c', 3: 'd'}


