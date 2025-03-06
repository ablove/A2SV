from collections import deque

class DataStream:
    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.queue = deque()
        self.val_count = 0

    def consec(self, num: int) -> bool:
        if len(self.queue) == self.k:
            val = self.queue.popleft()
            if val == self.value:
                self.val_count -= 1

        self.queue.append(num)
        if num == self.value:
            self.val_count += 1

        return self.val_count == self.k
