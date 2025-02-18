class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        total, count = 0, 0
        freq = defaultdict(int)
        freq[0] = 1 
        
        for num in nums:
            total += num 
            rem = total % k 
            
            if rem < 0:
                rem += k 
            
            if rem in freq:
                count += freq[rem] 
            
            freq[rem] += 1
        
        return count        






        