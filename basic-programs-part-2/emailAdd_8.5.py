fname = input('Enter file name: ')
try :
    fh = open(fname)
except :
    print('File cannot be found')
    quit()

count = 0
for line in fh :
    if line.startswith('From ') : 
        count = count + 1
        new_line = line.rstrip().split()
        print(new_line[1])
print('There were' , count, 'lines in the file with From as the first word')
