1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 无需做判断
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
遍历一遍
用target减去数组中的每个元素，把不存在map中的元素放入map，如果target-element在map中可找到，则就是答案
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i, num in enumerate(nums):
            if target - num in m:
                return [m[target-num], i]
            m[num] = i
        return []

Key: for+map结合
