class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l, r = 0, 0
        a, b = len(word1), len(word2)
        ans = []
        while l < a and r < b:
            ans.append(word1[l])
            ans.append(word2[r])
            l += 1
            r += 1
        while l<a:
            ans.append(word1[l])
            l += 1
        while r<b:
            ans.append(word2[r])
            r += 1

        return "".join(ans)        


        # Time O(A + B)
        # Space O(A + B)
        