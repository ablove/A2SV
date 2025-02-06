class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        a=len(nums)
        count=0

        for i in range(a):
            for j in range(i+1,a):
                if nums[i]==nums[j] and (i*j)%k==0:
                    count += 1
        return count








        
          




        







