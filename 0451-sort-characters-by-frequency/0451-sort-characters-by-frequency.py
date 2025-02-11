class Solution:
    def frequencySort(self, s: str) -> str:

        count_freq = defaultdict(int)

        for i in s:
            count_freq[i] += 1

        sorted_count = sorted(count_freq.items(), key=lambda x: x[1], reverse=True)
        
        ans = ""

        for key,value in sorted_count:
            ans += key * value

        return ans    















        