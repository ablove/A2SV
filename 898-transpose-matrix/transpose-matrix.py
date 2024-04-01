class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_len = len(matrix)
        colum_len = len(matrix[0])
        transposed = [[0] * row_len for _ in range(colum_len)]
        for i in range(row_len):
            for j in range(colum_len):
                transposed[j][i] = matrix[i][j]
        return transposed           