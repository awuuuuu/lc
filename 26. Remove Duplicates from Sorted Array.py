26. Remove Duplicates from Sorted Array
# 题目没看清楚，修改数组没理解
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        for i in range(1, len(nums)):
            if nums[curr] != nums[i]:
                curr = curr + 1
                nums[curr] = nums[i]
        return curr + 1     

Key: for + 两个指针
