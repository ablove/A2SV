class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        sum_subarray = 0
        min_length = float('inf')

        for right in range(len(nums)):
            sum_subarray += nums[right]

            while sum_subarray >= target:
                min_length = min(min_length, right - left + 1)
                sum_subarray -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0

            
        