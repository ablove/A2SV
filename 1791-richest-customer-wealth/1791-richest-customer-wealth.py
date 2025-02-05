class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_list = []
        for i in range(len(accounts)):
            summ = 0
            for j in range(len(accounts[i])):
                summ += accounts[i][j]
            sum_list.append(summ)
        return max(sum_list)    

        