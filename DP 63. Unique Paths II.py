#数组永远有index设置和index的边界问题

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0 and len(obstacleGrid[0]) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        a = [[1]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                a[i][0] = 0
            else:
                a[i][0] = a[i-1][0]
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                a[0][j] = 0
            else:
                a[0][j] = a[0][j-1]
        for i in range(1, m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    a[i][j] = 0
                else:
                    a[i][j] = a[i-1][j] + a[i][j-1]
        return a[m-1][n-1]
