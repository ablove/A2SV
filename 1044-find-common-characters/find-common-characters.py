class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        answer =[]
        minWord = words[0]
        for s in words:
            minWord = minWord if len(minWord)<=len(s) else s
        for char in minWord:
            flag = True 
            for i, check in enumerate(words):
                if char not in check:
                    flag = False 
                else:
                    words[i] = check.replace(char, '', 1)
            if flag :
               answer.append(char)
        return answer 
            
          













        
        


            








            


        

    







        