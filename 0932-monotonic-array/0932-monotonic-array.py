class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = True
        decrease = True
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                decrease = False
            elif nums[i] < nums[i-1]:
                increase = False
        return increase or decrease