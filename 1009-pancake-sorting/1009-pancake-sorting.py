class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        def flip(k):
            arr[:k] = arr[:k][::-1] 
            
        result = []
        n = len(arr)

        for target in range(n, 0, -1):  
            idx = arr.index(target) 
            
            if idx == target - 1: 
                continue
            
            if idx != 0:  
                flip(idx + 1)  
                result.append(idx + 1)
            
            flip(target)  
            result.append(target)
        
        return result








        