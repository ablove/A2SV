class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = []
        while columnNumber > 0:
            columnNumber -= 1
            val = columnNumber % 26
            result.append(chr(65 + val))
            columnNumber //= 26 
        
        return "".join(result[::-1]) 

















        
        