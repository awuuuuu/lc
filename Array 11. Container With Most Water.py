
##第一次用DP，但是不对，上下没有依赖关系
#暴力搜索，超时
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(0, len(height)):
            j = 0
            k = len(height) -1
            while j < i:
                if res > height[i] * (i - j):
                    break
                if height[j] >= height[i]:
                    res = max(res, height[i] * (i - j))
                    break
                j = j+1
            while i < k:
                if res > height[i] * (k - i):
                    break
                if height[k] >= height[i]:
                    res = max(res, height[i] * (k - i))
                    break
                k = k-1
        return res
     
   #key两根指针移动  
   class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                res = max(res, height[l] * (r-l))
                l = l + 1
            else:
                res = max(res, height[r] * (r-l))
                r = r - 1

        return res
