class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        max_length = 0
        ab = set()

        for right in range(len(s)):

            while s[right] in ab:
                ab.remove(s[left])
                left += 1
            
            ab.add(s[right])
            max_length = max(max_length, len(ab)) 

        return max_length             






        