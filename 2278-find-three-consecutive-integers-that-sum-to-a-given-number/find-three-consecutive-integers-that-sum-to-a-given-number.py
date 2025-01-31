class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        else:
            mid_val = num // 3
            return [mid_val -1, mid_val, mid_val +1]     
           
        