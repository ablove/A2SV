class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix[0])):
            k = 0
            j = i 
            temp = matrix [k][i]
            while k < len(matrix) and  j < len(matrix[0]):
                if temp != matrix[k][j]:
                    return False
                k+=1
                j+=1
        for i in range(len(matrix)):
            l = 0
            m = i
            temp = matrix[i][l]
            while l < len(matrix[0]) and m < len(matrix):
                if temp != matrix[m][l]:
                    return False
                l+=1
                m+=1
        return  True 
