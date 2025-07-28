class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        secret_count = defaultdict(int)
        guess_count = defaultdict(int)

        for s_digit, g_digit in zip(secret, guess):
            if s_digit == g_digit:
                bulls += 1
            else:
                secret_count[s_digit] += 1
                guess_count[g_digit] += 1

        for digit in guess_count:
            cows += min(secret_count[digit], guess_count[digit])

        return f"{bulls}A{cows}B"
