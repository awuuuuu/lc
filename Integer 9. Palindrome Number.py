# 测试案例不够多，10,11,121,1211没有考虑
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False
        if x<10:
            return True
        y = 0
        while x>y: 
            y = y*10 +x%10
            if y == 0:
                return False
            x = int(x/10)
        if x == 0:
            return False
        return y == x or int(y/10) == x
