# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:

#         store = Counter(nums)
#         ans = []
#         for i in store: 
#             if store[i] == 2:
#                 ans.append(i)
#         return ans        

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        return result
