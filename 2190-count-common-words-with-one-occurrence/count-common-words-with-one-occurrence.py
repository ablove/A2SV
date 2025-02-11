class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        count1 = Counter(words1)
        count2 = Counter(words2)

        set1 = set(words1)
        set2 = set(words2)

        set3 = set1 | set2
        print(set3)
        
        count = 0
        for i in set3:
            if count1[i] == count2[i] == 1:
                count += 1

        return count        

        # for i in 


        