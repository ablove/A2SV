class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            total = 0
            required_days = 1
            for weight in weights:
                if total + weight > capacity:
                    required_days += 1
                    total = 0
                total += weight
            return required_days <= days
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid  
            else:
                left = mid + 1  
        
        return left
