#key: hashmap, key in nums.keys()看是去要比key in nums要慢
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for n in nums:
            if n in m:
                m[n] = m[n] + 1
            else:
                m[n] = 1
            if m[n] + 1 > len(nums)/2:
                return n
#另外一条思路  2，排序法：排序后，出现次数大于一半的肯定在中间
#O(n) O(1)解法，range(len(nums) - 1)出错半天未查出来
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        count = 1
        for j in range(1, len(nums)):
            if count == 0:
                m = nums[j]
                count = 1
            elif m == nums[j]:
                count = count + 1
            else:
                count = count -1
        return m
        
 
 
 
 
 #improvement 三元表达式，变量初始化为N
 
 class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
