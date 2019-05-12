
#看的答案，不过感觉之前自己也有思路
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) < 3:
            return None
        
        res = nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                s = nums[i] + nums[r] + nums[l]
                if s == target:
                    return s
                elif s > target:
                    r = r - 1
                else:
                    l = l + 1
                if abs(s-target) < abs(res-target):
                    res = s
        return res
