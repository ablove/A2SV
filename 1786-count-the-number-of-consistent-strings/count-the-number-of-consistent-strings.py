class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_allowed = set(allowed)
        # print(list_allowed)
        count = 0

        for word in words:
            if set(word) <= set_allowed:
                    count += 1

        return count









        