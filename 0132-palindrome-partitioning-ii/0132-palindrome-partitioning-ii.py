class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True  
            for j in range(i):
                if s[j] == s[i] and (i - j <= 2 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
        
        cuts = [0] * n
        for i in range(n):
            min_cut = i 
            for j in range(i + 1):
                if is_palindrome[j][i]:
                    min_cut = 0 if j == 0 else min(min_cut, cuts[j - 1] + 1)
            cuts[i] = min_cut
        
        return cuts[-1]