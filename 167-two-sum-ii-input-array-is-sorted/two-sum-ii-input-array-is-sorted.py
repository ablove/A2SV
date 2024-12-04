class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # for i in range(len(numbers)-1):
        #     for j in range(i+1,len(numbers)):
        #         sum=numbers[i]+numbers[j]
        #         if sum==target:
        #             return [i+1,j+1]
        # return []  
        # brootforced solution  

        # optimized one
        l, r = 0, len(numbers)-1
        while l<r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1,r+1]
            elif sum > target:
                r -= 1
            else:
                l += 1
         # Time: o(n)
         # Space : o(1)







        
           

        