class Solution:
    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1
        result = set()
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                result.add(arr[mid])
                break
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return list(result)

    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        result = set()
        
        for num in nums1:
            intersect = self.binary_search(nums2, num)
            if intersect:
                result.add(num)
        
        return list(result)


