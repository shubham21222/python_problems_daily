#qus:- Given an integer array nums, find the  subarray with the largest sum, and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        summation = 0
        maximum = nums[0]

        for i in nums:
            summation = summation + i
            maximum = max(maximum, summation)
            if summation < 0:
                summation = 0

        return maximum