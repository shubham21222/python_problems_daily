#qus:- Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count1 = None
        count = 0

        for num in nums:
            if count == 0:
                count1 = num
                count = 1
            elif num == count1:
                count += 1
            else:
                count -= 1

        return count1
