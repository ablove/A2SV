class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        dict1 = defaultdict(int)
        dict1[0] = 1
        n = len(nums)
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        # acc = 0
        for j in range(len(nums)):
            # acc = nums[j]
            prefix[j] = prefix[j-1] + nums[j]
        print(prefix)
        
        print(dict1) 
        count = 0

        for i in range(n):
            a = prefix[i] - goal
            if a in dict1:
                count += dict1[a]
            dict1[prefix[i]] += 1

        return count            




        # n = len(nums)
        # left = summ = count = 0

        # for i in range(n):
        #     summ += nums[i]

        #     while summ > goal:
        #         if nums[left] == 1:
        #             summ -= 1
        #         left += 1

        #     if summ == goal:
        #         count += 1
                
        # return count                
        


        












        