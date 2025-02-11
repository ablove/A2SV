class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort(reverse=True)

        total_coins = 0
        i = 0
        iterations = len(piles) // 3

        for _ in range(iterations):
        
            total_coins += piles[i + 1]
            i += 2

        return total_coins



























      
        