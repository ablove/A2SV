class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        store = defaultdict(int)
        n = len(bills)
        
        # for i in bills:
        #     if i == 5:
        #         store["5"] += 1
        #     if i == 10:
        #         store["10"] += 1
        # print(store)
        if bills[0] == 10 or bills[0] == 20:
            return False
        flag = True
        for i in range(n):

            if bills[i] == 5:
                store["5"] += 1

            elif bills[i] == 10:
                if store["5"] == 0:
                    flag = False
                store["5"] -= 1
                store["10"] += 1

            elif bills[i] == 20:
                if store["5"] < 3 and store["10"] == 0 or store["10"] > 0 and store["5"] == 0:
                    flag = False
                elif store["10"] > 0 and store["5"] > 0:    
                    store["5"] -= 1 
                    store["10"] -= 1
                elif store["5"] >= 3 and store["10"] == 0:
                    store["5"] -= 3

        return flag            










        
        





        