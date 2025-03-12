class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = deque()
        max_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()

            min_deque.append(nums[right])
            max_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length