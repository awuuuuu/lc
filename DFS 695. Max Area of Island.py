#DFS, grid[i][j] 的更新有错误

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_count = 0
        
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    grid[i][j] = 0
                    count = 0
                    while len(stack):
                        (p, q) = stack.pop()
                        count += 1
                        if p > 0 and grid[p-1][q] == 1:
                            stack.append((p-1, q))
                            grid[p-1][q] = 0
                        if q > 0 and grid[p][q-1] == 1:
                            stack.append((p, q-1))
                            grid[p][q-1] = 0
                        if p < m-1 and grid[p+1][q] == 1:
                            stack.append((p+1, q))
                            grid[p+1][q] = 0
                        if q < n-1 and grid[p][q+1] == 1:
                            stack.append((p, q+1))
                            grid[p][q+1] = 0
                    max_count = max(max_count, count)
        return max_count
