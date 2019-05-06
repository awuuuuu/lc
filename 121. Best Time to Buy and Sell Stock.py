# TODO
#Time limitexceeded
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        l = len(prices)
        for i in range(l):
            for j in range(i+1, l):
                res = max(res, prices[j] - prices[i])
        return res

#key: 一维数据二维化，寻找最低点即为最佳买入点
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0 
        res = 0
        minum = prices[0]
        for i, p in enumerate(prices):
            if p < minum:
                minum = p
            if p - minum > res:
                res = p - minum
        return res
