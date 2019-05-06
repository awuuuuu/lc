#非一遍过，判断key是否存在不能直接在object中查

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i, n in enumerate(numbers):
            if target - n not in m.keys():
                m[n] = i+1
            else:
                return [m[target - n], i+1]
        return []
