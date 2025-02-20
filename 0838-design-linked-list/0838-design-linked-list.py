class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()  # Dummy node simplifies the head handling
        self.tail = None  # Tail pointer for the last node
        self.length = 0  # To keep track of the list's length

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1  # Return -1 if the index is invalid
        cur_node = self.dummy.next
        for _ in range(index):
            cur_node = cur_node.next
        return cur_node.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next  # Point new node to the current head
        self.dummy.next = new_node  # Update the dummy node's next pointer
        if self.length == 0:
            self.tail = new_node  # If the list is empty, the new node is also the tail
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.dummy.next = new_node  # If list is empty, make the dummy node point to it
            self.tail = new_node  # Tail points to the new node
        else:
            self.tail.next = new_node  # Link the current tail's next to the new node
            self.tail = new_node  # Update tail to point to the new node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:  # Invalid index
            return
        if index == self.length:  # Adding at the tail
            self.addAtTail(val)
        else:
            cur_node = self.dummy
            for _ in range(index):
                cur_node = cur_node.next
            new_node = Node(val)
            new_node.next = cur_node.next
            cur_node.next = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:  # Invalid index
            return
        cur_node = self.dummy
        for _ in range(index):
            cur_node = cur_node.next
        # If we're deleting the last node, update the tail pointer
        if cur_node.next == self.tail:
            self.tail = cur_node
        cur_node.next = cur_node.next.next
        self.length -= 1
