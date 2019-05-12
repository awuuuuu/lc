#被index搞晕了，redo


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        rowStart = 0
        rowEnd = m-1
        colStart = 0
        colEnd = n-1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd+1):
                arr.append(matrix[rowStart][i])
            rowStart = rowStart + 1
            for i in range(rowStart, rowEnd+1):
                arr.append(matrix[i][colEnd])
            colEnd = colEnd - 1
            if rowStart <= rowEnd:
                for i in range(colEnd, colStart-1, -1):
                    arr.append(matrix[rowEnd][i])
            rowEnd = rowEnd - 1
            if colStart <= colEnd:
                for j in range(rowEnd, rowStart-1, -1):
                    arr.append(matrix[j][colStart])
            colStart = colStart + 1
        return arr
