class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        result = [""] * n  

        for char, index in zip(s, indices):  
            result[index] = char  

        return "".join(result) 






            



















        