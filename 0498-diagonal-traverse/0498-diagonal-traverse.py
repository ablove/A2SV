class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if not mat:
            return []
        
        m, n = len(mat), len(mat[0])
        diagonals = {}
        
        for i in range(m):
            for j in range(n):

                if (i + j) not in diagonals:
                    diagonals[i + j] = []

                diagonals[i + j].append(mat[i][j])
        
        result = []
        
        for d in range(m + n - 1):

            if d % 2 == 0: 
                result.extend(diagonals[d][::-1])
            else:  
                result.extend(diagonals[d])
        
        return result






        








        