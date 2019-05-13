#凡是有除以二的，都可以联想到位运算

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 1
        while i <= n:
            if i == n:
                return True
            i = i << 1
        return False
