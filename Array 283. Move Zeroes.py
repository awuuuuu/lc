#redo

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1
        l = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[count] = nums[i]
                count += 1
        while count < len(nums):
            nums[count] = 0
            count += 1
