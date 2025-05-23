class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
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





         










        