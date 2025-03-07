from collections import deque

class MyQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)  # Append to the right (end of the queue)

    def pop(self) -> int:
        return self.q.popleft()  # Remove from the left (front of the queue)

    def peek(self) -> int:
        return self.q[0]  # Get the front element without removing it

    def empty(self) -> bool:
        return not self.q  # Check if the deque is empty
