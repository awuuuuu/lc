#DP

from operator import add, sub
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        l = 0
        r = 0
        a = [[False] * len(s) for _ in s]
        for i in range(len(s)):
            a[i][i] = True
        #j外i内，右边上三角
        for j in range(len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if add(i, 1) == j or a[add(i, 1)][sub(j, 1)]:
                        if sub(r, l) < sub(j, i):
                            r = j
                            l = i
                        a[i][j] = True
        return s[l:add(r,1)]
