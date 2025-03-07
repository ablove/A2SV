class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []
        for i in logs:
            if i == "./" or (i  == "../" and len(stack) == 0):
                continue
            elif i == "../":
                stack.pop()
            else:
                stack.append(i)
        return len(stack)

        