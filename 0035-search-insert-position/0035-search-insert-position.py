class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)

        for i in range(n):
            if nums[i] == target:
                return i
        else:
            if max(nums) < target:
                return len(nums)
            if target <= nums[0]:
                return 0    
            for i in range(n-1):
                if nums[i] < target and nums[i+1] >= target:
                    return i+1
                 
                 









             


        