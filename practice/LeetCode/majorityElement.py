class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        print(majority_count)
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            print(count)
            if count > majority_count:
                return num

sol = Solution()
ret = sol.majorityElement([2,2,1,1,1,2,2])
print(ret)



            

