class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j] > nums[j+1]:
                    nums[j+1],nums[j]=nums[j],nums[j+1]
              
        indexes_after_sort = []
        for index in range(n):
            if target == nums[index]:
                indexes_after_sort.append(index)

        return indexes_after_sort    
    




        