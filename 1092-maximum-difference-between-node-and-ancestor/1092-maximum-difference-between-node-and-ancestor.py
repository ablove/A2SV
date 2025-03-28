class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_min, current_max):
            if not node:
                return current_max - current_min
            current_min = min(current_min, node.val)
            current_max = max(current_max, node.val)
            left = dfs(node.left, current_min, current_max)
            right = dfs(node.right, current_min, current_max)
            return max(left, right)
        return dfs(root, root.val, root.val)
