class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Handle the case with only one or two elements separately
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        # Initialize variables to keep track of the two possible sums
        sum_even = nums[0]
        sum_odd = max(nums[0], nums[1])

        # Iterate over the remaining elements starting from the third element
        for i in range(2, len(nums)):
            if i % 2 == 0:
                sum_even = max(sum_even + nums[i], sum_odd)
            else:
                sum_odd = max(sum_odd + nums[i], sum_even)

        # Return the maximum of the two sums
        return max(sum_even, sum_odd)