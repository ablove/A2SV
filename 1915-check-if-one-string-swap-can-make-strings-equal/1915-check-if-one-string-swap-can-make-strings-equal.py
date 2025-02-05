class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        store_s1 = set()
        store_s2 = set()
        for i in range(len(s1)):
            for j in range(len(s2)):

                if i == j and s1[i] != s2[j]:
                    count += 1
                    store_s1.add(s1[i])
                    store_s2.add(s2[j])
        if count == 0 or count ==2 and store_s1 == store_s2:
            return True
        else:
            return False


        