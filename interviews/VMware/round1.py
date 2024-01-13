# What is a thread?
# What is a process?
# When there is memory constarint, which is preferable, thread or process?
# Explain inheritance with real time example
# Output of code snippet:
#                       1. sum of two numbers and input fetched in runtime
# 2. 

a = [1,2,3,4,5]
print(a[3:0:-1]) # ans should be [4,3,2] 
# Syntax for printing list in reverse - listname[start:stop:-1] 

# 3.

# A0 = list(zip(('a','b','c','d')(1,2,3,4)))
# A1 = range(0,9)
# A2 = [x for x in A0 if A0 in A1]
# print(A2) # ans should be []

#Using OS module, check i a file is present in a directory
# Directory structure is:
#                       a0/
#                          a01/
#                          a02/
#                              a001
#find if a001is there

#Check if given paranthesis inputs are valid/invalid
#  ([{}]) -- valid
#  ([)} -- invalid
#  hint - verify that no of open brac = no pf close bacs
#       - using stack, check if the to most brac in the stack is the converse of the picked brac

# What was your best job and whae are your responsibilities?
class Solution:
    def __init__(self) -> None:
        pass

    def balanced_bracs(self,brac:str)->bool:
        brac = input()
        dic = {'(':')','{':'}','[':']'}
        stack=[]
        for b in brac:
            if b in dic.keys():
                stack.append(b)
            else:
                if not stack:
                    return False
                if dic[stack.pop()]!=b:
                    return False
        if stack:
            return False
        return True

bracs = Solution()
bracs.balanced_bracs("([)}")



