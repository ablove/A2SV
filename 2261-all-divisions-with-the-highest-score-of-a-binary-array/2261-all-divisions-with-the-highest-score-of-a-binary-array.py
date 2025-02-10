class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        n = len(nums)
        total_ones = sum(nums) 
        left_zeros = 0
        right_ones = total_ones
        max_score = 0
        result = []

        for i in range(n + 1): 

            score = left_zeros + right_ones 
            
            if score > max_score: 
                max_score = score
                result = [i]

            elif score == max_score: 
                result.append(i)

            if i < n and nums[i] == 0:  
                left_zeros += 1 

            if i < n and nums[i] == 1:
                right_ones -= 1

        return result


        
                    
                    
        
            
        
        