#DP问题，TODO
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_sum = nums[0]
        t = nums[0]
        for i in range(1,len(nums)):
            t = max(nums[i], nums[i]+t)
            if t> max_sum:
                max_sum = t
        return max_sum       
