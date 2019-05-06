#TODO，while 循环i,j未递增，res未累加，未一遍过


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        i = 0
        j = 1
        res = 0
        while j <= len(prices) - 1:
            if prices[j] > prices[i]:
                res = res + prices[j] - prices[i]
            i = i + 1
            j = j + 1
        return res
