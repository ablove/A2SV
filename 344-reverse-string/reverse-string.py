class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right =0, len(s)-1

        while left<right:

            s[left], s[right]= s[right], s[left]
            left += 1
            right -= 1
            
        return s    















        # # for i in range(len(s)//2):
        # #     s[i],s[-(i+1)]=s[-(i+1)],s[i]
        # # return s    

        # left, right = 0, len(s) - 1
        # while left <= right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1

     

        # # Time : o(n)
        # # Space : o(1)
         
