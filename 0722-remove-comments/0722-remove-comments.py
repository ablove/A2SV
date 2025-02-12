
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False  # Flag to check if we are inside a block comment
        in_block = False
        result, buffer = [], []

        for line in source:
            if not in_block:
                buffer = []
            i = 0
            while i < len(line):
                
                if line[i:i+2] == "/*" and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == "*/" and in_block:
                    in_block = False
                    i += 1
                elif not in_block and line[i:i+2] == "//":
                    break
                elif not in_block:
                    buffer.append(line[i])
                i += 1
            if buffer and not in_block:
                result.append("".join(buffer))
        
        return result
