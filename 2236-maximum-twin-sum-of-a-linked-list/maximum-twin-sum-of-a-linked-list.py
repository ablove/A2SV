# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        max_twin_sum = 0
        first, second = head, prev
        while second:
            max_twin_sum = max(max_twin_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_twin_sum
        