class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        # nums_dict = defaultdict(list)
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):

                if abs(nums[i] - nums[j]) == k and i<j:
                    count += 1

        return count            


            

        