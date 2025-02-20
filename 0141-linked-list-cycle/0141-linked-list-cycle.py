# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        dummy = ListNode(0, head)
        fast = slow = dummy

        flag = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                flag = True
                break 
                # slow = head

                # while fast:
                #     slow = slow.next
                #     fast = fast.next
        return flag      


        