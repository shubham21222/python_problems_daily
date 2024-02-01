class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        i = 0
        while i < n:
            if i + 2 < n and nums[i+2] - nums[i] <= k:
                result.append(nums[i:i+3])
                i += 3
            else:
                return []
        return result