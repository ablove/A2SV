# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        if count < k:
            return head
        
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        if curr:
            head.next = self.reverseKGroup(curr, k)
        
        return prev






