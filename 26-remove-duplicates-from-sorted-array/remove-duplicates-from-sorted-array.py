class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        # Initialize the slow pointer
        slow = 0

        # Iterate with the fast pointer
        for fast in range(1, len(nums)):
            # If we find a new unique value
            if nums[fast] != nums[slow]:
                # Move the slow pointer forward
                slow += 1
                # Update the value at slow with the unique value
                nums[slow] = nums[fast]

        # Return the count of unique elements
        return slow + 1
        

        

    
        

        
        