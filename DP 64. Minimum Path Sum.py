#for循环 in range（k）,结束后i = k-1.......
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = [[0]*len(grid[0]) for i in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    m[i][j] = grid[0][0]
                elif i == 0:
                    m[i][j] = m[i][j-1] + grid[i][j]
                elif j == 0:
                    m[i][j] = m[i-1][j] + grid[i][j]
                else:
                    m[i][j] = min(
                        m[i-1][j-1] + min(grid[i][j-1],grid[i-1][j]),
                        m[i][j-1],
                        m[i-1][j]
                    ) + grid[i][j]

        return m[i][j]
