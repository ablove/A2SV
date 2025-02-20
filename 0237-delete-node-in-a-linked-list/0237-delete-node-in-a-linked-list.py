# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next 

        # dummy = ListNode(0)  
        # dummy.next = head  
        # prev = dummy 
        
        # while prev.next and prev.next != node:
        #     prev = prev.next
        
        # if prev.next:
        #     prev.next = prev.next.next
        
        # return dummy.next 
