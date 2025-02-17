class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        acc = 0
        n = len(nums)
        prefix_sum = [0] * len(nums)

        for i in range(len(nums)):

            acc += nums[i]
            prefix_sum[i] = acc 
        
        if prefix_sum[-1] - prefix_sum[0] == 0:
            return 0

        for i in range(1,n):

            left = prefix_sum[i-1] 
            right = prefix_sum[-1] - prefix_sum[i]

            if left == right:
                return i
        else:
            return -1
            