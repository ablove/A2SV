class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * (cars ** 2)
        
        def canRepairInTime(mid):
            return sum(int(math.sqrt(mid // rank)) for rank in ranks) >= cars
        
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
