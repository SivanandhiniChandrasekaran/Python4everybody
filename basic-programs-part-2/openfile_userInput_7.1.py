# Use words.txt as the file name
fname = input("Enter file name: ")
try :
    fh = open(fname , 'r')
except:
    print('File cannot be found')
    quit()
    
for line in fh :
    line = line.rstrip()
    print(line.upper())