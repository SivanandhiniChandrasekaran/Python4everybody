fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print('File cannot be found')
    quit()

result = list()

for line in fh :
    words = line.strip().split()
    print(words)
    for word in words :
        print(word) 
        if word not in result :
            result.append(word)
            print(result)
result.sort()
print(result)
