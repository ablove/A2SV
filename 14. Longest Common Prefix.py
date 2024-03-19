class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:  # Check if the array is empty
            return ""

        prefix = strs[0]  # Initialize prefix with the first string

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]  # Remove last character from prefix

                if not prefix:  # If prefix becomes empty, return ""
                    return ""

        return prefix
                
