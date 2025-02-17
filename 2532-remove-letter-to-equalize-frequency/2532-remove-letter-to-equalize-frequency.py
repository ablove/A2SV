class Solution:
    def equalFrequency(self, word: str) -> bool:


        for i in range(len(word)): 

            temp_word = word[:i] + word[i+1:] 
            count = Counter(temp_word) 

            if len(set(count.values())) == 1:
                return True
                
        return False  
        