# list to string

things = input ("enter input")
tins = things.split()
print(tins)

lam =[]
for tin in tins:
    if tin not in lam:
        lam.append(tin)
print(lam)

newstr = ''.join(lam)
print(newstr)

stg = newstr[::-1]#reversing a string
print(stg)

#OR

nwstr = ""
for st in lam:
    nwstr += st
print(nwstr)