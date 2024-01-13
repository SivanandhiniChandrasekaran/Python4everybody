fhand = input("enter file name:")
fh = open(fhand)

result = list()
for line in fh:
    words= line.split()
    for word in words:
        if word not in result:
            result.append(word)
print(result)
#new = list(dict.fromkeys(result))
#end = list(new)
#print(new)
