class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        n = len(nums)
        l = len(set(nums))

        if l <3:
            return max(nums)
        nums_set = list(set(nums))
        nums_set.sort(reverse=True)
        return nums_set[2]

    


            








        