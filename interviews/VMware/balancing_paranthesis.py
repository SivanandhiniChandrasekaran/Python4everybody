
class Solution:
    def __init__(self) -> None:
        pass

    def balanced_bracs(self,brac:str)->bool:
        #brac = input()
        dic = {'(':')','{':'}','[':']'}  #
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
brac = input()

#another way to check if
if bracs.balanced_bracs(brac):
    print("balanced")
else:
    print("not balanced")
