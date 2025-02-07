class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:

        count = Counter(s)
        # print(count)

        if letter in count:
            return floor((count[letter]/len(s)) * 100)
        else:
            return 0    





















        