from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        list1 = [set(word) for word in words]
        count =0
        for i in range(len(list1)):
            for j in range(len(list1)):
                if list1[i]==list1[j] and i!=j:
                    count += 1
        return count//2           






        
        
        
        




        