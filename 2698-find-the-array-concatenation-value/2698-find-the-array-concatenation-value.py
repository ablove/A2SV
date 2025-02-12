class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        n = len(nums)
        concat_value = 0
        left, right = 0, n-1

        if len(nums) %2 == 1:
            concat_value += int(str(nums[n//2]))

        while left < right:
            concat_value += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1

        return concat_value   



            

        