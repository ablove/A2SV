class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        rows, cols = len(img), len(img[0])

        ans = [[0] * cols for i in range(rows)]

        def inbound(x,y):
            return 0 <= x < rows and 0<= y < cols

        for i in range(rows):
            for j in range(cols):
                arr =[(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1, j+1)]

                count, summ = 1, img[i][j]
                for val in arr:

                    x,y = val[0], val[1]

                    if inbound(x,y):
                        count += 1
                        summ += img[x][y]
                ans[i][j] = (summ//count)
        return ans


                
                






        