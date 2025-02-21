class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # n = len(candies)
        # ans = [] * n
        # for i in range(n):
        #     candies[i] += extraCandies
        #     val = candies[i]
        #     for j in range(n):
        #         if candies[j] > val:
        #             # print(candies[i] , i ,val)
        #             ans.append(False)
        #             break
        #     else:
        #         ans.append(True)
        #     candies[i] -= extraCandies    
        #     # print(candies)
        # return ans 


        ## Optimized One

        n = len(candies)
        ans = [] * n
        max_num = max(candies)

        for i in range(n):
            candies[i] += extraCandies
            if candies[i] >= max_num:
                ans.append(True)
            else:    
                ans.append(False)
        return ans        





         










        