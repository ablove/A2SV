from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # convert list to set for O(1) lookup
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # base case: empty string is always segmentable

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # no need to check further if one match is found

        return dp[n]
