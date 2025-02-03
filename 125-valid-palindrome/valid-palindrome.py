class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right =0, len(s)-1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
        return True    

    # Time Complexity O(n)
    # Space Complexity O(1)
    







        























        # n = len(s)
        # l = 0
        # r = n - 1

        # while l < r:
        #     if not s[l].isalnum():
        #         l += 1
        #         continue
        #     if not s[r].isalnum():
        #         r -= 1
        #         continue

        #     if s[l].lower() != s[r].lower():
        #         return False
        #     else:
        #         l += 1
        #         r -= 1    
                
        # return True        



         


      

        