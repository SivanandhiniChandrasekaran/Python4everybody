# counting no. of vowels in a string

def count_vowels():
    string=input("Enter string:")
    vowels=0
    for i in string:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    print("Number of vowels are:")
    print(vowels)

def count_consonants():
    count =0
    string1 = input("Enter a word")
    vowels1 = ("a","e","i","o","u")

    for a in string1:
        if a not in vowels1:
            count = count+1
    print("Number of consonants are:")
    print(count)
        


def remove_vowels():
    strings=input("Enter string:")
    vowels = ("a","e","i","o","u")
    for x in strings:
        if x in vowels:
            nwstr = strings.replace(x,"")
    print(nwstr)

def print_vowels():
    strings=input("Enter string:")
    vowels = ("a","e","i","o","u")
    for x in strings:
        if x in vowels:
            print(x)

    
print_vowels()
remove_vowels()
count_vowels()
count_consonants()