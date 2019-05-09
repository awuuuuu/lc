#错了
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) ==0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        t = [[0]*n for i in matrix]
        v = 0
        for i in range(m):
            t[i][0] = int(matrix[i][0])
            v = max(v, t[i][0])
        for j in range(n):
            t[0][j] = int(matrix[0][j])
            v = max(v, t[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    t[i][j] = min(t[i-1][j-1], t[i][j-1], t[i-1][j]) + 1
                    v = max(v, t[i][j])
        return v*v
