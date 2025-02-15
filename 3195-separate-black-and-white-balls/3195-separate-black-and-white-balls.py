class Solution:
    def minimumSteps(self, s: str) -> int:

        left, swaps = 0, 0  

        for right in range(len(s)):
            if s[right] == '0':  
                swaps += right - left  
                left += 1  

        return swaps        


        