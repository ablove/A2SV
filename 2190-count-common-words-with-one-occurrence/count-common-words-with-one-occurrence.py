class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        count1 = Counter(words1)
        count2 = Counter(words2)

        count = 0
        for i in count1:
            if count1[i] == count2[i] == 1:
                count += 1

        return count        

        # for i in 


        