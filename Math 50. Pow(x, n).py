#self.myPow重复调了两次，一次就够了

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        t = abs(n)
        res = self.myPow(x*x, int(t/2))
        if t%2:
            res = res * x
        if n < 0:
            return 1/res
        return res
