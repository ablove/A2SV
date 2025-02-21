class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        n = len(candies)
        ans = [] * n
        for i in range(n):
            candies[i] += extraCandies
            val = candies[i]
            for j in range(n):
                if candies[j] > val:
                    # print(candies[i] , i ,val)
                    ans.append(False)
                    break
            else:
                ans.append(True)
            candies[i] -= extraCandies    
            # print(candies)
        return ans           




        