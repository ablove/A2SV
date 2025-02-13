class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        summ = 0
        right = k

        for i in range(k):
            summ += nums[i]
        
        max_avg = summ/k
        
        for i in range(1, n-k+1):
            summ += -nums[i-1] + nums[right]
            cur_avg = (summ) / k
            max_avg = max(max_avg, cur_avg)
            right += 1
            print(max_avg)

        return max_avg   




