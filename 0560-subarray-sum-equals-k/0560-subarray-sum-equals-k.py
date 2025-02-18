class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

    # Initialize the hashmap to store prefix sums and their counts
        prefix_sum_counts = {0: 1}  # Base case: prefix sum 0 is counted once
        current_sum = 0
        count = 0
        
        for num in nums:
            # Update the current cumulative sum
            current_sum += num
            
            # Check if there exists a subarray whose sum equals k
            if current_sum - k in prefix_sum_counts:
                count += prefix_sum_counts[current_sum - k]
            
            # Update the hashmap with the current cumulative sum
            if current_sum in prefix_sum_counts:
                prefix_sum_counts[current_sum] += 1
            else:
                prefix_sum_counts[current_sum] = 1
        
        return count

        
        