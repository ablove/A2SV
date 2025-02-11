class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        min_num = min(nums)
        max_num = max(nums)
        
        # Step 2: Create a count array to store the frequency of each number
        # We use (max_num - min_num + 1) size to cover all numbers from min_num to max_num
        count = [0] * (max_num - min_num + 1)
        
        # Step 3: Populate the count array with the frequency of each number
        for num in nums:
            count[num - min_num] += 1
        
        # Step 4: Rebuild the sorted array
        sorted_nums = []
        for i in range(len(count)):
            sorted_nums.extend([i + min_num] * count[i])
        
        return sorted_nums



        















        



        
        


        