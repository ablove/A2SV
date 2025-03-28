from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        
        def canPlaceBalls(min_force):
            count, last_pos = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= min_force:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False
        
        while left < right:
            mid = (left + right + 1) // 2
            if canPlaceBalls(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
