class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(firstNuum, path):
            if len(path) == k:  
                ans.append(path[:])
                return
            for candidate in range(firstNuum, n+1):
                path.append(candidate)  
                backtrack(candidate + 1, path) 
                path.pop()
        backtrack(1,[])
        return ans
        
        



        