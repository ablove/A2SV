class Solution:
    def maxArea(self, height: List[int]) -> int:

        area = []
        left, right = 0, len(height)-1

        while left<right:
            a = (right - left) * min(height[left], height[right])
            area.append(a)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max(area)            



















        # l, r = 0, len(height)-1
        # Max = 0

        # while l < r:
        #     min_height = min(height[l], height[r])
        #     width = r-l
        #     max_area = min_height * width
        #     Max = max(Max, max_area)

        #     if height[l] >= height[r]:
        #         r -= 1
        #     else:
        #         l += 1    

        # return Max  





























       
#         n = len(height)
#         l = 0
#         r = n - 1
#         max_area = 0

#         while l < r:
#             w = r - l
#             h = min(height[l], height[r])
#             a = w * h
#             max_area = max(max_area, a)
            
#             if height[l] < height[r]:
#                 l += 1
#             else:
#                 r -= 1

#         return max_area

# # Time Complexity: O(n)
# # Space Complexity: O(1)   
































