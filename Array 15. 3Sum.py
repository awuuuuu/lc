#重做，很多边界情况需要考虑

class Solution:
    # -4 -1 -1 0 1 2
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums)<=2:
            return []
        nums.sort()
        if nums[len(nums) - 1] < 0 or nums[0] > 0:
            return []
        i = 0
        j = len(nums)-1
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) -1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s >0:
                    r -= 1
                else:
                    l += 1
                    
        return res
