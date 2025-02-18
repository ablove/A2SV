class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        
        nums.sort(reverse=True)
        
        prefix = [0] * (n + 1) 
        for start, end in requests:
            prefix[start] += 1
            if end + 1 < len(prefix):
                prefix[end + 1] -= 1 
        
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        
        prefix.pop()
        
        prefix.sort(reverse=True)
        
        max_sum = sum(a * b for a, b in zip(nums, prefix)) % MOD
        
        return max_sum




