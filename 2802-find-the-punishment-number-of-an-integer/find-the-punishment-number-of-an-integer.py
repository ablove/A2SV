class Solution:
    def can_partition(self, s: str, target: int, index=0, current_sum=0) -> bool:
        if index == len(s):
            return current_sum == target

        num = 0
        for i in range(index, len(s)):
            num = num * 10 + int(s[i])
            if current_sum + num > target:
                break
            if self.can_partition(s, target, i + 1, current_sum + num):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            if self.can_partition(str(i * i), i):
                total += i * i
        return total

