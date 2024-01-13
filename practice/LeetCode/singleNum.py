class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
                print(no_duplicate_list)
            
            else:
                no_duplicate_list.remove(i)
                print(no_duplicate_list)
        return no_duplicate_list.pop()
        

sol = Solution()
ret = sol.singleNumber([4,1,2,1,2])
print(ret)