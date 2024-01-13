# getting email addresses from mbox-short.txt

fhand = input("enter file name:")
fh = open(fhand)

result = []
count = 0
for line in fh:
    if line.startswith('From:'):
        print(line)
        count = count +1
        addr= (line[6:]) # email addr starts from the 6th index
        print(count,addr)

        if addr not in result:
            result.append(addr)
print(result)



#converting list to string
newstr = ""
for st in result:
    newstr += st
print(newstr)




    
#edit = addr([:])