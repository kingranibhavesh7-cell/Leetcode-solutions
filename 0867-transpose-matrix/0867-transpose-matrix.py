class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        col = len(matrix[0])
        transpose = [[0 for _ in range (rows) ] for _ in range (col)]
        for i in range (rows):
            for j in range(col):
                transpose[j][i] = matrix[i][j]
        return transpose
