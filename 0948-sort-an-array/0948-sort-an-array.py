class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)

        return merge(left_half,right_half)

    def merge(left,right):
        result = []
        i = 0
        j = 0

        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1
        
        result += left[i:]
        result += right[j:]

        return result