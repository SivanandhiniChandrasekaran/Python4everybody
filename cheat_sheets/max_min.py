num = input("enter nums:")
numb = num.split()
print(numb)
for n in numb:
    a=max(numb)
    b=min(numb)
print("max num is:",a)
print("min num is:",b)

#OR

aa = input("enter nums:")
bb = aa.split()
a=max(bb)
b=min(bb)
print("max num is:",a)
print("min num is:",b)