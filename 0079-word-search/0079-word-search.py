class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, index):
            # Check if we found the word
            if index == len(word):
                return True
            
            # Check boundaries and if the current cell matches the current character
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]):
                return False
            
            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all directions: down, up, right, left
            found = (backtrack(r + 1, c, index + 1) or 
                     backtrack(r - 1, c, index + 1) or 
                     backtrack(r, c + 1, index + 1) or 
                     backtrack(r, c - 1, index + 1))
            
            # Restore the original cell value
            board[r][c] = temp
            
            return found
        
        # Start backtracking from each cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):  # Start searching from this cell
                    return True
        
        return False