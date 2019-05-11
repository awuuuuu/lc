#redo


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #124231
        l = len(nums)
        if l <= 1:
            return
        i = l-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i = i - 1
        if i == -1:
            nums.reverse()
            return
        j = -1
        for j in range(l-1, i, -1):
            if nums[i] < nums[j]:
                break
        nums[i], nums[j] = nums[j], nums[i]
        r = l -1
        l = i + 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        
        #or nums[i+1::]
        nums[i+1:len(nums)] = nums[i+1:len(nums)][::-1]
