class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                index = stack.pop()
                prev_index = stack[-1] if stack else -1
                result += arr[index] * (i - index) * (index - prev_index)
                result %= MOD
            stack.append(i)
        
        while stack:
            index = stack.pop()
            prev_index = stack[-1] if stack else -1
            result += arr[index] * (len(arr) - index) * (index - prev_index)
            result %= MOD
        
        return result
