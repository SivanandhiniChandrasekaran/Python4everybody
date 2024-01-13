fhand = input("Enter file name:")
try :
    fh = open(fhand)
except:
    print("File can't be found")
    quit()

counts = dict()
for lines in fh:
    words = lines.split()
    for word in words:
        if word not in counts:            
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
print(counts["sun"])
