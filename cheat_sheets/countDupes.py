def rmv_lst_duplicates():   
    fhand = input("enter file name:")
    fh = open(fhand)

    result = list()
    for line in fh:
        words= line.split()
        for word in words:
            if word not in result:
                result.append(word)
    print(result)
    print(len(result))

def count_duplicates():   
    fhand = input("enter file name:")
    fh = open(fhand)

    dupe = dict()
    for line in fh:
        words= line.split()
        
        for a in words:
            if a not in dupe:
                dupe[a] = 1
            else:
                dupe[a] = dupe[a]+1

    print(dupe)
    print(dupe["computer"])

rmv_lst_duplicates()
count_duplicates()