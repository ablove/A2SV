class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        
        duplicate = -1
        missing = -1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicate = nums[i]
                missing = i + 1
                break
        
        return [duplicate, missing]
