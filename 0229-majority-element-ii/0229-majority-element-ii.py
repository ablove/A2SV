class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freq = defaultdict(int)  
        n = len(nums)
        ans = []

        for num in nums:
            freq[num] += 1

        for num, count in freq.items():
            if count > n // 3:
                ans.append(num)
                
        return ans





        # count = Counter(nums)
        # n = len(nums)
        # ans = []

        # for num in count:
        #     if count[num] > (n // 3):
        #         ans.append(num)
        # return ans

        


        
        
         

            



        