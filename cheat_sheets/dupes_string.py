word = input("enter word:")

result = list()
for letter in word:
    letters = letter.split()
    print(letters)
    for l in letters:
        if l not in result:
            result.append(l)
print(result)
result.sort()

#list to string 
string = ""
for z in result:
    string += z
print(string)

# reverse a string
def reverse(str):   
    str = str[::-1]
    return str 

s = "JavaTpoint"  
print ("The original string  is : ",s)   
print ("The reversed string using extended slice operator  is : ",reverse(s)) 


