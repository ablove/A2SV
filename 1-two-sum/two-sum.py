class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = defaultdict(list)
        for i,num in enumerate(nums):
            count[num].append(i)
        # print(count) 

        for num in count:
            diff = target - num
            if num == diff and len(count[num]) > 1:
                return [count[num][0], count[num][1]]
                
            if (diff) in count and num != diff:
                return [count[num][0], count[diff][0]]





        


        
            


