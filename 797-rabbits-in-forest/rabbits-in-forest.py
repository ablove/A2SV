class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total_rabbits = 0
        
        for k, freq in count.items():
            total_rabbits += math.ceil(freq / (k + 1)) * (k + 1)
        
        return total_rabbits
