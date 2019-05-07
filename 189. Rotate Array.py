#TODO 不停地错，函数index边界值问题，k>len(nums)的情况考虑错误


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #前一段数组往右移动时，第一个元素把最后一个元素覆盖了
        if k >= len(nums):
            k = k % len(nums)
        t=[]
        for i in range(len(nums)-k):
            t.append(nums[i])
        for i in range(len(nums)-k, len(nums)):
            nums[i - len(nums) + k] = nums[i]
        for i in range(len(nums)-k):
            nums[i + k] = t[i]
  
  
