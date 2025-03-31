class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        left, right = 1, max(candies)
        
        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)
            
            if count >= k:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
