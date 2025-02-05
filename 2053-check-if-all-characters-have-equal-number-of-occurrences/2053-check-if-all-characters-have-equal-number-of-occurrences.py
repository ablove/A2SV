class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        # print(count)

        freq = set(count.values())
        # print(freq)
        if len(freq) == 1:
            return True
        else:
            return False    

            







        