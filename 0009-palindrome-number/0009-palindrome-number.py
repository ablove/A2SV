class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_val = str(x)
        reverse_str = str_val[::-1]
        if str_val == reverse_str:
            return True
        return False
           
      
       

        


        