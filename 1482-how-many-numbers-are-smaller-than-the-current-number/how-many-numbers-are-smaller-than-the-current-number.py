class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        ans = [0] * len(nums)

        for i in range(len(nums)):
            for x in nums:

                if x < nums[i]:
                    ans[i] +=  1
                    
        return ans            














        # return [sum(1 for x in nums if x < nums[i]) for i in range(len(nums))]





        

        