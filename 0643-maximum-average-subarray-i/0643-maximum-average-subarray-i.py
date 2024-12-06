class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
        max_avg = curr_sum / k

        for i in range(k,n):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            avg2 = curr_sum / k
            max_avg = max(max_avg, avg2)
        return max_avg    


# Time complexity   O(n)
# Space complexity   O(1)

        