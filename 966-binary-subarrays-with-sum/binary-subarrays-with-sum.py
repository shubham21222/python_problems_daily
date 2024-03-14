class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq_sums = collections.defaultdict(int)
        result, current, n = 0, 0, len(nums)

        # main logic
        freq_sums[0] = 1
        for i in range(n):
            current += nums[i]
            result += freq_sums[current - goal]
            freq_sums[current] += 1

        return result