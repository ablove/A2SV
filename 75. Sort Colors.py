class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a=len(nums)
        for i in range(a):
            for j in range(a-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        print(nums)   
