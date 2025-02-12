class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        ans = []
        len1 = len(nums1)
        len2 = len(nums2)
        left, right = 0, 0

        while left < len1 and right < len2:

            if nums1[left][0] == nums2[right][0]:
                ans.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
                left += 1
                right += 1

            elif nums1[left][0] < nums2[right][0]:
                ans.append([nums1[left][0], nums1[left][1]])
                left += 1

            else:
                ans.append([nums2[right][0], nums2[right][1]])
                right += 1

        while left < len1 and right == len2:
            ans.append([nums1[left][0], nums1[left][1]])
            left += 1

        while left == len1 and right < len2:
            ans.append([nums2[right][0], nums2[right][1]])
            right += 1  

        return ans     

            








        