class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Initialize current_sum and max_sum to the first element of nums
        current_sum = nums[0]
        max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Either start a new subarray with current num, or continue with the existing subarray
            current_sum = max(num, current_sum + num)
            
            # Update max_sum if we found a larger subarray sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum


            
                












        