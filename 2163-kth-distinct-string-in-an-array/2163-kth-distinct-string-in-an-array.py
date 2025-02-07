class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        count = Counter(arr)

        distinct_strings = [val for val in arr if count[val] == 1]

        return distinct_strings[k-1] if k <= len(distinct_strings) else ""
        