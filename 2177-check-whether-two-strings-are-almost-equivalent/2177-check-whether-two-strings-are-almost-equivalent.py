class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        count_word1 = Counter(word1)
        count_word2 = Counter(word2)

        unique_chars = set(word1) | set(word2)

        for char in unique_chars:
            if abs(count_word1[char] - count_word2[char]) > 3:
                return False
        
        return True       






        