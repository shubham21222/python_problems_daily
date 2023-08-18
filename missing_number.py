#qus:- Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        
        for i in range(n + 1):
            total ^= i
            
        for num in nums:
            total ^= num
            
        return total
