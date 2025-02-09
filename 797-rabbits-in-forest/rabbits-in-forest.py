class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        count = Counter(answers) 
        total_rabbits = 0

        for x, y in count.items():
            
            groups = math.ceil(y / (x + 1)) 
            total_rabbits += groups * (x + 1) 

        return total_rabbits
        