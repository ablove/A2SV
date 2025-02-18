class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum_counts = {0: 1} 
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            if current_sum - k in prefix_sum_counts:
                count += prefix_sum_counts[current_sum - k]
            
            if current_sum in prefix_sum_counts:
                prefix_sum_counts[current_sum] += 1
            else:
                prefix_sum_counts[current_sum] = 1
        
        return count

        













        
        