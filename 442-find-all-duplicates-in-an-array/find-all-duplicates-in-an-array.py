class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        store = Counter(nums)
        ans = []

        for i in store:
            
            if store[i] == 2:
                ans.append(i)

        return ans        



        