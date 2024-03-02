class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort()
        new_arr = []
        for i in range(len(nums)):
            result = nums[i] ** 2    
            new_arr.append(result)
            new_arr.sort()
        return new_arr