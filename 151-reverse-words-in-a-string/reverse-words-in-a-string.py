class Solution:
    def reverseWords(self, s: str) -> str:

        list1 = s.split()
        list1.reverse()
        return str(" ".join(list1))





        