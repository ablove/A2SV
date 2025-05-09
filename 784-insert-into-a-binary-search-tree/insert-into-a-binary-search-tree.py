
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(root, val):
            if root is None:
                return TreeNode(val)

            if val > root.val:
                root.right = insert(root.right, val)
            else:
                root.left = insert(root.left, val)

            return root  
        
        return insert(root, val) 
