
#Key: 公式
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1] * (rowIndex + 1)
        for i in range(1, rowIndex/2 + 1):
            res[i] = res[rowIndex - i] = res[i - 1] * (rowIndex - i + 1) / i
        return res
