#只考虑了半边

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        m = len(M)
        if m == 0:
            return 0
        i = 0
        count = 0
        while i < m:
            if M[i][i] == 1:
                stack = []
                M[i][i] = 0
                count += 1
                for j in range(m):
                    if M[i][j] == 1:
                        stack.append(j)
                while len(stack):
                    j = stack.pop()
                    if M[j][j] == 1:
                        M[j][j] = 0
                        for k in range(m):
                            if M[j][k] == 1:
                                stack.append(k)
            i = i + 1
        return count          
