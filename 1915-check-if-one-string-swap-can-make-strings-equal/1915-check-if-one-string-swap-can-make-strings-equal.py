class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        store_s1 = set()
        store_s2 = set()
        for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                    store_s1.add(s1[i])
                    store_s2.add(s2[i])
        if count == 0 or count ==2 and store_s1 == store_s2:
            return True
        else:
            return False


        