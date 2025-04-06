import bisect
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def find_closest_heater(house):
            idx = bisect.bisect_left(heaters, house)
            if idx == 0:
                return heaters[0]
            if idx == len(heaters):
                return heaters[-1]
            left_heater = heaters[idx - 1]
            right_heater = heaters[idx]
            return left_heater if abs(left_heater - house) <= abs(right_heater - house) else right_heater
        
        return max(abs(house - find_closest_heater(house)) for house in houses)
