class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n
        answer = [1] * n



        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        # print(prefix_product)
        for i in range(n-2, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i+1]
        
        # print(suffix_product)

        for i in range(n):
            answer[i] = prefix_product[i] * suffix_product[i]


        return answer











    
            


    


    
        