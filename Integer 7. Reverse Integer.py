#pow(2,31)的限制遗漏，不用重做

from operator import mul, mod, floordiv
class Solution:
    def reverse(self, x: int) -> int:
        if x > (pow(2,31) -1) or x<(-pow(2,31)):
            return 0
        t = abs(x)
        res = 0
        while t>0:
            res = mul(res, 10) + mod(t, 10)
            t = floordiv(t, 10)
        if res > (pow(2,31) -1) or res<(-pow(2,31)):
            return 0    
        return res if x>0 else -res
