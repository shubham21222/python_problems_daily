#qus:- Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#[4,5,6,7,0,1,2] if it was rotated 4 times.
#[0,1,2,4,5,6,7] if it was rotated 7 times.
#Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#You must write an algorithm that runs in O(log n) time.

class Solution(object):
    def findMin(self, nums) :
        start = 0
        end = len(nums) - 1

        while start < end:
            middle = start + (end - start) // 2

            if nums[middle] > nums[end]:
                start = middle + 1
            else:
                end = middle

        return nums[start]

