#TODO 再刷
#两根指正+map用于重复元素长度计算不太合适
#错误的解决方案，用map存储重复元素的index,两根指针位置相减，但是长度和指针位置的计算依赖于index，导致判断条件很多，逻辑很复杂，无法理清楚所有的情况
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
        	return len(s)
        m = {}
        i = 0
        j = 0
        max_len = 1
        while j < len(s):
            if s[j] in m:
                if max_len < j - i:
                    max_len = j - i
                if m[s[j]] > i:
                	i = m[s[j]] + 1
                if i == j:
                    #有重复的字母就更新map，而非将map.clear()
                    m.clear()
            m[s[j]] = j
            j = j + 1
        #j在while循环中未计算完毕
        if i == 0:
        	return len(s)
        else:
        	max_len = max(max_len, j-i)
        return max_len  
