class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t

        s1 = sorted(s)
        t1 = sorted(t)    
        count_s = Counter(s1)
        count_t = Counter(t1)
        
        for i in count_t:

            if count_t[i] > count_s[i]:
                return i

                  







        