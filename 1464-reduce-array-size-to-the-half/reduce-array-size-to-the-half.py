class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        frequencies = sorted(freq.values(), reverse=True)
        
        removed = 0
        count = 0
        half = len(arr) // 2

        for f in frequencies:
            removed += f
            count += 1
            if removed >= half:
                return count
