class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_len = result = 0
        for i in range(len(nums)):

            if nums[i] == 1:
                result += 1
                max_len = max(result, max_len)
            else:
                result = 0
        return max_len        

                


        