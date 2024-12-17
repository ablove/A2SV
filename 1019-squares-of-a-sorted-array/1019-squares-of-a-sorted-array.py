class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right =0, len(nums)-1
        ans = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans.append(abs(nums[left]) ** 2)
                left += 1
            else:
                ans.append(abs(nums[right])** 2)   
                right -= 1
        ans.reverse()        
        return ans         


















        
        # left, right = 0, len(nums) - 1

        # list1 = []
        # while left <= right :
        #     if abs(nums[left]) > abs(nums[right]):
        #         list1.append(nums[left] ** 2)
        #         left += 1
        #     else:
        #         list1.append(nums[right] ** 2)
        #         right -= 1
        # list1.reverse()
        # return list1

        # # time: O(n)
        # # space : O(1)
        



            


























          

        




