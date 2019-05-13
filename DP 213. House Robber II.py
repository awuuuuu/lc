
#之前写的都有点忘了。。。

class Solution:
    # 2 3 2 3 1
    # a[i] = max(a[i-1], a[i-2] + n[i])
    def rob(self, nums: List[int]):
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.rob_o(nums[0:len(nums)-1]), self.rob_o(nums[1:len(nums)]))
    def rob_o(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        prev = nums[0]
        nex = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if prev+nums[i] > nex:
                nex, prev = prev+nums[i], nex
            else:
                prev = nex
        return nex  
