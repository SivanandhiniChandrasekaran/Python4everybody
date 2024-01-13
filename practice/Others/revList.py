
def rev_list():
    lis = [100, 200, 300, 400, 500]
    boss = lis[::-1]

    print(boss)

def add_list_indexwise():
    list1 = ["M", "na", "i", "Ke"] 
    list2 = ["y", "me", "s", "lly"] 
    c = zip(tuple(list1),tuple(list2))
    print("HELLOOO",tuple(c)) #HELLOOO (('M', 'y'), ('na', 'me'), ('i', 's'), ('Ke', 'lly'))

    # syntax for list comprehension --> 
    # newlist = ["expression" "for" "item" "in" "iterable" "condition to be performed"]
    list3 = [x+y for x,y in zip(list1,list2)] #['My', 'name', 'is', 'Kelly']
    print(list3)

def list_square():
    aList = [1, 2, 3, 4, 5, 6, 7]
    ross = [x*x for x in aList]
    print(ross)

def list_conct_indexwise():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    rach = [i+j for i in list1 for j in list2]   #['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
    print(rach)

def list_front_rev():
#Given a two Python list. Iterate both lists simultaneously such that list1 should display item in 
# original order and list2 in reverse order
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]

    for x, y in zip(list1, list2[::-1]):
        print(x, y)

def rmv_emtyStr_list():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    resList = list(filter(None, list1))
    print(resList)

def add_item_list():
    #Add item 7000 after 6000 in the following Python List
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)
    print(list1)

def add_item_list_extnd():
    #add h,i,j as elemets and not list
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sublist = ["h", "i", "j"]
    list1[2][1][2].extend(sublist)
    print("HIIIIIII",list1)

def findandReplace():
    list1 = [5, 10, 15, 20, 25, 50, 20]

    val = list1.index(20)
    list1[val] = 200

    print(list1)

def removeItem():
    list1 = [5, 20, 15, 20, 25, 50, 20]
    for val in list1:
        if val == 20:
            list1.remove(val)
    print(list1)




rev_list()
add_list_indexwise()
list_square()
list_conct_indexwise()
list_front_rev()
rmv_emtyStr_list()
add_item_list()
add_item_list_extnd()
findandReplace()
removeItem()