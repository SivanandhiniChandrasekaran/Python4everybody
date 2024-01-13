#string palindrome
ent = input("enter a string")

if ent == ent[::-1]:
    print("it is a palindrome")
else:
    print("No, its not a palindrome")