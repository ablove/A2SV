class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        min_num = min(nums)
        max_num = max(nums)
        
        count = [0] * (max_num - min_num + 1)
        
        for num in nums:
            count[num - min_num] += 1
        
        sorted_nums = []
        for i in range(len(count)):
            sorted_nums.extend([i + min_num] * count[i])
        
        return sorted_nums
