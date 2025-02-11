class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        for i in range(len(s)):

            x = s.find(part) 
            if x != -1:
                s = s.replace(part, "", 1)

        return s        


        


        


        