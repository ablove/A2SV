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

        left, right = 0, len(numbers) - 1

        while left < right :
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
                break
            elif sum > target:
                right -= 1
            else:
                left += 1



        
         # Time: o(n)
         # Space : o(1)








        
           

        