class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        for x in range(n, 1, -1):
            max_index = arr.index(x)
            if max_index != x - 1:
                if max_index != 0:
                    result.append(max_index + 1)
                    arr = arr[:max_index + 1][::-1] + arr[max_index + 1:]
                result.append(x)
                arr = arr[:x][::-1] + arr[x:]
        return result









        