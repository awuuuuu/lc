#o(n)空间复杂度是简单的，不过有很多睿智用了O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = [0] *(len(nums)+2)
        for i in nums:
            if i <= len(nums) and i > 0:
                n[i] = 1
        for i in range(1, len(n)):
            if n[i] == 0:
                return i
   
   #o(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0     
        l = len(nums)
        nums.append(0)
        nums.append(0)
        while i < l:
            if nums[i] <= l and nums[i] > 0 and nums[nums[i]] != nums[i]:
                t = nums[i]
                nums[i] = nums[t]
                nums[t] = t
            else:
                i += 1
        for i in range(1, len(nums)):
            if nums[i] != i:
                return i                
