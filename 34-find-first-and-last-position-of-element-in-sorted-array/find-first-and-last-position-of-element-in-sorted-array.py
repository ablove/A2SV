from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = last = -1

        def first_position(l, r):
            nonlocal first
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    if nums[mid] == target:
                        first = mid
                    r = mid - 1  
            return first

        def last_position(l, r):
            nonlocal last
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    if nums[mid] == target:
                        last = mid
                    l = mid + 1 
            return last

        ans1 = first_position(0, len(nums) - 1)
        ans2 = last_position(0, len(nums) - 1)

        return [ans1, ans2]
