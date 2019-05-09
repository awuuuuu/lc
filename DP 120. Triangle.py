#上一层走到下一层的index对应出错
from operator import floordiv,sub
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        m = len(triangle)
        n = len(triangle[-1])
        t = [0] * n
        for i in range(m):
            for j in range(len(triangle[i])-1, -1, -1):
                if j == sub(len(triangle[i]), 1):
                    t[j] = t[j-1] + triangle[i][j]
                elif j == 0:
                    t[j] = t[j] + triangle[i][j]
                else:
                    t[j] = min(t[j], t[j-1]) + triangle[i][j]
        return min(t)
