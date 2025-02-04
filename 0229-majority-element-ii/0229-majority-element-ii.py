class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        ans = []

        for num in count:
            if count[num] > (n // 3):
                ans.append(num)
        return ans 

            



        