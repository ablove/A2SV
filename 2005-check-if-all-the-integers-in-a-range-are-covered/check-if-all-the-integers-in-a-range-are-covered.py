class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        covered_nums = set() 
        
        for interval in ranges:
            for num in range(interval[0], interval[1] + 1):
                covered_nums.add(num)
        
        for num in range(left, right + 1):
            if num not in covered_nums:
                return False 
                
        return True 
            



        


        








        