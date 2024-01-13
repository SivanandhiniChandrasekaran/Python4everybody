#Given a string of odd length greater than 7, return a new string made of the middle three characters
#  of a given String
def mid3strings():
    str1 = "JhonDipPeta"
    
    length = int((len(str1)-3)/2)
    final =str1[length:length+3]
    print(final)

#Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
def string_append():
    s1 = "Ault"
    s2 = "Kelly"
    length = int(len(s2)/2)
    s3 = s1[:length]+s2+s1[-length: ]
    print(s3)

#Given two strings, s1, and s2 return a new string made of the first, middle, 
# and last characters each input string
def fst_mdl_lst():
    s1 = "America"
    s2 = "Japan"
    s3 = s1[0]+s2[0]+s1[int(len(s1)/2)]+s2[int(len(s1)/2)-1]+s1[-1]+s2[-1]
    print(s3)

#Arrange string characters such that lowercase letters should come first
def string_case_order():
    str1 = "PyNaTive"
    lower = []
    upper = []
    for char in str1:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    sorted_string = ''.join(lower + upper)
    print("arranging characters giving precedence to lowercase letters:")
    print(sorted_string)

#Count all lower case, upper case, digits, and special symbols from a given string
def string_count_allTypes():
    str1 = "P@#yn26at^&i5ve"
    lower_count = 0
    upper_count = 0
    digits_count = 0
    splChar_count = 0

    for char in str1:
        if char.islower():
            lower_count +=1
    
        
        if char.isupper():
            upper_count += 1
     

        if char.isdigit():
            digits_count += 1
    

        else:
            splChar_count = len(str1)-(lower_count+upper_count+digits_count)

    print("No of lower chars in the given string is: ", lower_count)   
    print("No of uper chars in the given string is: ", upper_count)  
    print("No of digits in the given string is: ", digits_count)      
    print("No of special chars in the given string is: ", splChar_count) 

def check():
    s1 = "Ynf"
    s2 = "PYnative"
    if s1 in s2:
        print("string is balanced")
    else:
        print("no, String is not balanced:")

#Find all occurrences of “USA” in a given string ignoring the case
def find_usa():
    count = 0
    str1 = "Welcome to USA. usa awesome, isn't it?"
    output = str1.lower().split()
    print(output)
    for out in output:
        if "usa" in out:
            count += 1
    print("The USA count is:", count)

#Given a string, return the sum and average of the digits 
# that appear in the string, ignoring all other characters

def sum_of_digits():
    str1 = "English = 78 Science = 83 Math = 68 History = 65"
    newstr = str1.split()

    digits = []
    for new in newstr:
        if new.isnumeric():
            digits.append(new)
    print(digits)

    nums =[]
    for digit in digits:
        for dig in digit:
            nums.append(dig)
        print(nums)
            
    dg_sum = 0
    nos = len(nums)
    print(nos)
    for num in nums:
        dg_sum = int(num) + dg_sum
    print("sum of digits is:", dg_sum)
    average = dg_sum/nos
    print("Average is :", average)

# Given an input string, count occurrences of all characters within a string
def count_occurances():
    str1 = "Apple"
    counts = dict()
    names = []
    for s in str1:
        names.append(s)
    print(names)

    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] += 1
    print(counts)





mid3strings()
string_append()
fst_mdl_lst()
string_case_order()
string_count_allTypes()
check()
find_usa()
sum_of_digits()
count_occurances()