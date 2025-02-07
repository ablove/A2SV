class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        count = Counter(nums)
        count_pairs = 0
        count_singles = 0  
        # ans = []

        for num in count:
            count_pairs += count[num] //2
            count_singles += count[num] %2
                      
        return [count_pairs, count_singles]        
















        