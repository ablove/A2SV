class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stk = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue

            while stk and c < stk[-1] and last[stk[-1]] > i:
                seen.remove(stk.pop())

            stk.append(c)
            seen.add(c)

        return "".join(stk)
