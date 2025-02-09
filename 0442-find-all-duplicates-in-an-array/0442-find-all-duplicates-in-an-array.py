class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        store = Counter(nums)
        # print(store)
        ans = []

        for i in store:
            
            if store[i] == 2:
                ans.append(i)

        # print(ans)
        return ans        



        