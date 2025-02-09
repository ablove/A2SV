class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = Counter(nums)
        # print(count[4])

        for num in count.keys():
            if count[num] > (n//2):
                return num













        