class Solution(object):
    def merge(self, nums1, m, nums2, n):

        merged = []
        left = right = 0
        
        while left < m and right < n:

            if nums1[left] < nums2[right]:
                merged.append(nums1[left])
                left += 1

            else:
                merged.append(nums2[right])
                right += 1
        print(merged)

        while left == m and right < n:
            merged.append(nums2[right])
            right += 1

        while left < m and right == n:
            merged.append(nums1[left])
            left += 1 

        for i in range(n + m):
            nums1[i] = merged[i]  


