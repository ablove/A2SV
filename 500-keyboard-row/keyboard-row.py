class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        ans = []
        lst1 = list("qwertyuiop")
        lst2 = list("asdfghjkl")
        lst3 = list("zxcvbnm")

        for word in words:

            if all(chr in lst1 for chr in word.lower()):
                ans.append(word)
            elif all(chr in lst2 for chr in word.lower()):
                ans.append(word)
            elif all(chr in lst3 for chr in word.lower()):
                ans.append(word)        

        return ans

                

































        # ans = []

        # # set_words = set()
        # keyboard1 = set("qwertyuiop")
        # keyboard2 = set("asdfghjkl")
        # keyboard3 = set("zxcvbnm")

        # for word in words:
        #     if word <= keyboard1 or word <= keyboard2 or word <= keyboard3:
        #         ans.append()
        # return ans        


        


        