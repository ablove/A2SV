class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        if maxDoubles == 0:
            return target - 1
        
        count = 0
        while maxDoubles > 0 and target > 2:
            if target % 2 == 0:
                count += 1
                target //= 2
                maxDoubles -= 1
            else:
                count += 2
                target //= 2
                maxDoubles -= 1
        count += (target - 1)
        return count        







        