def rmv_str_dup():
    given = input("enter a string: ")

    sets = []
    for letter in given:
        if letter not in sets:
            sets.append(letter)
    print(sets)

    newstr = "".join(sets)
    print(newstr)

rmv_str_dup()
