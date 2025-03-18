# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
         
        stack = []  
        def inOrder(node):
            if not node:
                return 
            inOrder(node.left)
            stack.append(node.val)
            inOrder(node.right)
        inOrder(root) 

        if 1 <= k <= len(stack):
            return stack[k-1]
        else:
            raise ValueError("k is out of range")
    
        


                





        