class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter((nums))
        ans = []
        for num in count:
            if count[num] == 2:
                ans.append(num)
        return ans        
        