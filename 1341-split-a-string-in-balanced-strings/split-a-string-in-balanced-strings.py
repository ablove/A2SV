class Solution:
    def balancedStringSplit(self, s: str) -> int:

        count_r = 0
        count_l = 0
        count_ans = 0

        for i in range(len(s)):
            if s[i] == "L":
                count_l += 1
                if count_l == count_r:
                    count_ans += 1
                    count_l = count_r = 0
            else:
                count_r += 1
                if count_l == count_r:
                    count_ans += 1
                    count_l = count_r = 0
        return count_ans            


            
                     



        