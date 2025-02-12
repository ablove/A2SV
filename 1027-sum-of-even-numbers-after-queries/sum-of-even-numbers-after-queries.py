class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

    #    The bruteforce approach
        # answer = []

        # for i in range(len(nums)):
        #     summ = 0
        #     nums[queries[i][1]] += queries[i][0]
            
        #     for j in nums:
        #         if j % 2 == 0:
        #             summ += j
            

        #     answer.append(summ)

        # return answer
    

    #  The optimized one

        result = []
        even_sum = sum(x for x in nums if x % 2 == 0)  
        
        for val, index in queries:
            if nums[index] % 2 == 0: 
                even_sum -= nums[index]
            
            nums[index] += val 
            
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            
            result.append(even_sum) 
        
        return result       
































        # ans = []
        # for indx,val in enumerate(queries):
        #     nums[indx] += val

        #     summ = 0
        #     for num in nums:
        #         if num%2 ==0:
        #             summ += num
        #             ans.append(summ)
        # return ans
        

        
                            












        