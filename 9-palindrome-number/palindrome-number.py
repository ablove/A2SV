class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = str(x)
        reverse_str = ans[::-1]
        if ans == reverse_str:
            return True
        return False    
       

        


        