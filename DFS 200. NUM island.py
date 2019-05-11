

#DFS 速度感觉比较慢
from operator import add, sub
def DFS(grid, i, j):
    print(i,j)
    if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0":
        return
    grid[i][j] = "0"
    DFS(grid, add(i, 1), j)
    DFS(grid, i, add(j,1))
    DFS(grid, i, sub(j,1))
    DFS(grid, sub(i,1), j)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    DFS(grid, i, j)
                    count = add(count, 1)
        return count
