class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = 2 * (n - 1)  
        time %= cycle 

        if time < n: 
            return 1 + time
        else: 
            return 2 * n - 1 - time
            













        