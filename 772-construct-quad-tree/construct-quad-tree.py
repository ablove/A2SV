class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isLeaf(x1, y1, x2, y2):
            """ Check if all values in the grid from (x1, y1) to (x2, y2) are the same. """
            first_val = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] != first_val:
                        return False, None
            return True, first_val
        
        def build(x1, y1, x2, y2):
            """ Recursively build the Quad-Tree. """
            leaf, val = isLeaf(x1, y1, x2, y2)
            if leaf:
                return Node(val == 1, True, None, None, None, None)
            else:
                mid_x = (x1 + x2) // 2
                mid_y = (y1 + y2) // 2
                return Node(
                    False,
                    False,
                    build(x1, y1, mid_x, mid_y),     # top-left
                    build(x1, mid_y, mid_x, y2),     # top-right
                    build(mid_x, y1, x2, mid_y),     # bottom-left
                    build(mid_x, mid_y, x2, y2)      # bottom-right
                )
        
        return build(0, 0, len(grid), len(grid[0]))