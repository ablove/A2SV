class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(1 for x in nums if x < nums[i]) for i in range(len(nums))]

        
