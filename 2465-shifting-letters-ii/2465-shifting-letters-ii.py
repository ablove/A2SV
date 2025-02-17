class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        prefix = [0] * (n + 1)

        for shift in shifts:
            start, end, direction = shift
            if direction == 0:
                prefix[start] -= 1
                if end + 1 < n:
                    prefix[end + 1] += 1
            else:
                prefix[start] += 1
                if end + 1 < n:
                    prefix[end + 1] -= 1  

        for j in range(1, n):
            prefix[j] += prefix[j - 1]

        ans = []
        for k in range(n):
            new_letter = ((ord(s[k]) - ord('a') + prefix[k]) % 26) + ord('a')
            ans.append(chr(new_letter))

        return "".join(ans)   

