class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maximum = nums[0]
        operation = 0

        for i in range(1, len(nums)):
            if nums[i] < maximum:
                maximum = nums[i]
                operation += i

        return operation