class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if (len(segment) == 1 or segment[0] != '0') and int(segment) <= 255:
                        backtrack(start + length, path + [segment])
        
        backtrack(0, [])
        return result