class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        n = len(nums)
        ans = []
        max_xor = 0

        for i in range(n):
            for j in range(n):

                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    ans.append([nums[i], nums[j]])
        # print(ans)
        for i in range(len(ans)):
            cur_xor = ans[i][0] ^ ans[i][1]
            max_xor = max(max_xor, cur_xor)

        return max_xor        







        