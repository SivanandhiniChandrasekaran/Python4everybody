fname = input('Enter file name: ')
try :
    fh = open(fname)
except :
    print('File cannot be found')
    quit()

counts = dict()

for line in fh :
    if line.startswith('From ') :
        words = line.split()
        addr = words[1]
        print(addr)
        counts[addr] = counts.get(addr,0)+1
print(counts)

bigCount =  None
bigWord = None
for word,count in counts.items() :
    if bigCount is None or count>bigCount:
        bigCount = count
        bigWord = word
print(bigWord, bigCount)

