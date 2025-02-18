class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        freq = defaultdict(int)
        freq[0] = 1
        
        total, count = 0, 0
        
        for num in nums:
            total += num  
            
            if (total - k) in freq:
                count += freq[total - k]
            
            freq[total] += 1 
        
        return count

        













        
        