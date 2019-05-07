118. Pascal's Triangle
#每一行按照index累加，数组index range问题
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        cur = 0
        res = []
        while cur <= numRows -1:
            if cur == 0:
                res.append([1])
            else:
                tmp = []
                for i in range(cur+1):
                    if i == 0 or i == cur:
                        tmp.append(1)
                    else:
                        tmp.append(res[cur - 1][i - 1] + res[cur - 1][i])
                res.append(tmp)
            cur  = cur + 1
        return res
