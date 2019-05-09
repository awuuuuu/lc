#重做
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = {}
        for i in wordDict:
            m[i] = True
        #创建一维数组，不能用False * 8
        d = [False for i in s]
        for i in range(len(s)):
        #判断key是否存在，不能用m[key]
            if i == 0 and s[i] in m:
                d[i] = True
                #边界情况+1遗漏
            for j in range(i+1):
                if j == 0:
                    if s[j:i+1] in m:
                        d[i] = True
                        break
                elif d[j-1] and (s[j:i+1] in m):
                    d[i] = True
                    break
        return d[-1]
