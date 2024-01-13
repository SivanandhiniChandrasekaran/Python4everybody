fname = input("Enter file name:")
fh = open(fname)

result=[]
for lines in fh:
    print(lines)
    words= lines.split()
    print(words)
    for word in words:
        print(word)
        if word not in result:
            result.append(word)

print(result)
#sorts in ascending 
result.sort()
print(result)

#sorts in descending
result.sort(reverse = True)
print(result)

#reverses the list
result.reverse()
print(result)

#deletes the index 2 and displays the deleted item
x =result.pop("and")
print(x)


