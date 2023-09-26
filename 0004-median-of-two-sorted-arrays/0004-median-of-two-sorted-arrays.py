class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
    
        n = len(nums1)
        if n % 2 == 0:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (nums1[mid1] + nums1[mid2]) / 2
        else:
            mid = n // 2
            return nums1[mid]