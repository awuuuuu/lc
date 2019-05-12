#这道题真是错了无数遍啊

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if  s[0] == '0':
            return 0
        a = [0] * (len(s)+1)
        a[1] = 1
        a[0] = 1
        for i in range(1,len(s)):
            t = int(s[i-1:i+1])
            if t == 0 or s[i] == '0' and int(s[i-1]) >= 3:
                return 0
            if t <= 26 and t>=11 and t != 20:
                a[i+1] = a[i] + a[i-1]
            elif t == 20 or t == 10:
                a[i+1] = a[i-1]
            else:
                a[i+1] = a[i]
        return a[len(s)]
