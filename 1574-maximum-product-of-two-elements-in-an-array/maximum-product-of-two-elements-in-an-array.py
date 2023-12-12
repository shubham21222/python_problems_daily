class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)-1
        nums.sort()
        return (nums[n]-1)*(nums[n-1]-1)
        