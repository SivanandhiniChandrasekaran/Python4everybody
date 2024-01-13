fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print('File cannot be found')
    quit()

count = 0
ival = 0
for line in fh :
    if line.startswith('X-DSPAM-Confidence:'):
        x = line.find('0')
        y = float(line[x:])
        count = count + 1
        ival = ival + y
fh.close()

print('Total no count :' , count)
print('Total :' , ival)
Average = ival / count
print('Average spam confidence:' , Average)
