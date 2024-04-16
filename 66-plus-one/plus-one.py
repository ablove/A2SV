class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_integer=int(''.join(map(str,digits)))
        ans=digits_integer + 1
        
        digit_list = list(map(int, str(ans)))
        return digit_list





        







        