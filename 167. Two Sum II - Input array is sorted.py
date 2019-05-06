# TODO
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

    #已排序数组和未排序数组的区别在于，两根指针相对而行
    class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) <= 1:
            return []
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[j] + numbers[i] > target:
                j = j - 1
            elif numbers[j] + numbers[i] < target:
                i = i + 1
            else:
                return [i+1, j+1]
        return []
    
    优化1
    class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            #必定存在一解
            if numbers[j] + numbers[i] == target:
                return [i+1, j+1]
            elif numbers[j] + numbers[i] < target:
                i = i + 1
            else:
                j = j - 1
