class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort(reverse=True)
        a,b,c = 0,1,2
        while c<n: 
            if nums[b] + nums[c] > nums[a]:
                return nums[b] + nums[c] + nums[a]
            else:
                a += 1
                b += 1
                c += 1
        return 0        


















        