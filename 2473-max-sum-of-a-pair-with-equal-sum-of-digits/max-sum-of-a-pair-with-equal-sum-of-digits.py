class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        digit_map = defaultdict(list)
        max_sum = -1
        
        for num in nums:
            d_sum = digit_sum(num)
            digit_map[d_sum].append(num)
        
        for key in digit_map:
            if len(digit_map[key]) > 1:
                digit_map[key].sort(reverse=True)
                max_sum = max(max_sum, digit_map[key][0] + digit_map[key][1])
        
        return max_sum





        