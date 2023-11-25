from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        lsum = 0
        total_sum = sum(nums)

        for i in range(0, len(nums)):
            diff = abs(nums[i] * i - lsum + (total_sum - lsum - nums[i] * (len(nums) - i)))
            lsum += nums[i]
            result.append(diff)

        return result
