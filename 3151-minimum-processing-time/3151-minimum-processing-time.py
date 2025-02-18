class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        processorTime.sort(reverse=True)
        
        tasks.sort()
        
        max_time = 0
        n = len(processorTime)
        
        for i in range(n):
            max_time = max(max_time, processorTime[i] + tasks[(i + 1) * 4 - 1])  
        
        return max_time    
        