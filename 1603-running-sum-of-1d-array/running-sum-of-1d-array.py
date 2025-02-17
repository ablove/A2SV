class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # running_sum = [0] * len(nums)
        # running_sum[0] = nums[0]

        for i in range(1,len(nums)):

            nums[i] += nums[i-1]
            # running_sum[i] = running_sum[i-1] + nums[i]
        return nums
        # return running_sum 






        