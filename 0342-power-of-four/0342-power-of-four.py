class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        def poower(n):
            if n == 0:
                return False
            if n == 1:
                return True
            if n % 4 == 0:
                n = n // 4
            else:
                return False
            return poower(n)

        abe = poower(n) 
        return abe




        