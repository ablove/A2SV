class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(left_array, right_array):
            left, right = 0, 0
            merged = []

            while left < len(left_array) and right < len(right_array):
                if left_array[left] <= right_array[right]:
                    merged.append(left_array[left])
                    left += 1
                else:
                    merged.append(right_array[right])
                    right += 1   
            while left < len(left_array):
                merged.append(left_array[left])
                left += 1

            while right < len(right_array):
                merged.append(right_array[right])
                right += 1
            return merged    

        def merge(nums):
            # left, right = 0, -1
            if len(nums) <= 1:
                return nums

            mid = (len(nums)-1) //2
            left_array = merge(nums[:mid+1])
            right_array = merge(nums[mid+1:])
            # print(left_array, right_array)
            return mergeSort(left_array, right_array)

        return merge(nums)    

        # min_num = min(nums)
        # max_num = max(nums)
        
        # count = [0] * (max_num - min_num + 1)
        
        # for num in nums:
        #     count[num - min_num] += 1
        
        # sorted_nums = []
        # for i in range(len(count)):
        #     sorted_nums.extend([i + min_num] * count[i])
        
        # return sorted_nums
