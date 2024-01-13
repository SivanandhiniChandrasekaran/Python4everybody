def vowel_cons_pair(st):
    vowels = ("a","e","i","o","u")
    size = len(st)

    count =0
    for x in range(size-1):
        # If the xth character is not found in the set vowels, 
        # means it is a consonant 
        # And if the (x+1)th character is found in the set vowels, 
        # means it is a vowel 
        # We increment the count of such pairs 
        if (st[x] not in vowels and st[x+1] in vowels):
            count += 1
    print(count)


# Python Program to Count Vowels and Consonants in a String
def countVowelsConsonants():
    str1 = input("Please Enter Your Own String : ")
    vowels = 0
    consonants = 0

    for i in str1:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
        or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    
    print("Total Number of Vowels in this String = ", vowels)
    print("Total Number of Consonants in this String = ", consonants)
            

vowel_cons_pair("entreprenuer")
countVowelsConsonants()
