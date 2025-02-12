class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(heights)
        
        for i in range(n):
            for j in range(0, n-i-1):
                
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
        
        return names

        # Insertion Sort
        # for i in range(1, n):
        #     key_height = heights[i]
        #     key_name = names[i]
        #     j = i - 1
        #     while j >= 0 and heights[j] < key_height:
        #         heights[j + 1] = heights[j]
        #         names[j + 1] = names[j]
        #         j -= 1
        #     heights[j + 1] = key_height
        #     names[j + 1] = key_name
        # return names

        # Selection Sort
        # for i in range(n):
        #     max_index = i
        #     for j in range(i+1, n):
        #         if heights[j] > heights[max_index]:
        #             max_index = j
        #     heights[i], heights[max_index] = heights[max_index], heights[i]
        #     names[i], names[max_index] = names[max_index], names[i]
        # return names

        # Counting Sort (assuming heights have a known max value)
        # max_height = max(heights)
        # count = [0] * (max_height + 1)
        # mapping = {}
        # for i in range(n):
        #     count[heights[i]] += 1
        #     mapping[heights[i]] = names[i]
        # sorted_names = []
        # for h in range(max_height, -1, -1):
        #     while count[h] > 0:
        #         sorted_names.append(mapping[h])
        #         count[h] -= 1
        # return sorted_names


        