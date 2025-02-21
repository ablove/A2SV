class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)

        if n == 3 and len(set(arr)) != n:
            return False
  
        val = max(arr)
        max_num = arr.index(val)
        

        if max_num == n-1 or max_num == 0:
            return False  

        if len(arr[:max_num]) != len(set(arr[:max_num])) or len(arr[max_num+1:]) != len(set(arr[max_num+1:])):
            return False 
        
        arr1 = sorted(arr[:max_num]) 
        arr2 = sorted(arr[max_num+1:], reverse=True)
        print(arr1)
        print(arr2)
        
        if arr[:max_num] == arr1 and arr[max_num+1:] == arr2:
            return True
        else:
            return False







        