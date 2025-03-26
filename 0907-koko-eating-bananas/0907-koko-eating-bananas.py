class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        ans = 1

        def good(rate):
            total_number = 0

            for pile in piles:
                total_number += (ceil(pile/rate))
            return total_number <= h

        while l <= r:
            mid = (l+r) // 2

            if good(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans                    



        