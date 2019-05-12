#脑子不清楚了


import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return math.inf if divident > 0 else -math.inf
        if dividend == 0:
            return 0
        sign = (dividend < 0) is (divisor < 0)
        if divisor == 1 or divisor == -1:
            r = dividend if divisor == 1 else -dividend
            return min(max(-2147483648, r), 2147483647)
        dividend,divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            count = 1
            tmp = divisor
            while dividend >= tmp<<1:
                tmp = tmp << 1
                count = count << 1
            dividend -= tmp
            res += count
        return res if sign else -res
