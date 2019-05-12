#最大公约数计算，记住

def common(a,b):
    while b:
        a, b = b, a%b
    return a
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_count = 0
        
        n = len(points)
        if n <= 2:
            return n
        
        for i in range(n):
            overlap = 0
            m = {}
            count = 1
            for j in range(i+1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                key = 'd'
                if x == 0 and y == 0:
                    overlap += 1
                    continue
                if x == 0:
                    m[key] = m[key] + 1 if key in m else 1
                else:
                    t = common(x,y)
                    if t:
                        x = x/t
                        y = y/t
                    key=(x,y)
                    m[(x,y)] = m[(x,y)] + 1 if (x,y) in m else 1
                count = max(count, m[key]+1)
            max_count = max(count+overlap, max_count)
        return max_count
