class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        str=""
        a=0
        for i in range(len(s)):
            if a<len(spaces) and i==spaces[a]:
                str+=" "
                a+=1
            str+=s[i]
        return str        