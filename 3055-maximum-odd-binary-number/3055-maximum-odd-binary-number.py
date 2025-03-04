class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        if s == "0":
            return

        list1 = Counter(s)
        ans = ""
        # for i in list1:
        print(list1["0"])
        ans += "1" * (list1["1"]-1)
        ans += "0" * list1["0"]
        ans += "1"
        return ans    
        # # print(list1)







        