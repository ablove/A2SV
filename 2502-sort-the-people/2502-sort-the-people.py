class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(heights)

        for i in range(n-1):
            for j in range(i+1, n):

                if heights[j] > heights[i]:

                    heights[i], heights[j] =  heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]

        
        return names 












        
        # for i in range(n-1):

        #     min_index=i
        #     for j in range(i+1,n):
        #         if heights[j] < heights[min_index]:
        #             min_index=j
        #     heights[i], heights[min_index] = heights[min_index], heights[i]
        #     names[i], names[min_index] = names[min_index], names[i]   

        # return names
          




          




















