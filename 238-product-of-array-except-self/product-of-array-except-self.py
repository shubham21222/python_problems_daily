class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = 1
        s = []
        if nums.count(0) > 1:
            for i in range(len(nums)):
                s.append(0)
            return s 
        elif 0 in nums: 
            for i in nums:
                if i != 0:
                    sum *= i
            index = nums.index(0)
            nums[index] = sum
            for i in range(len(nums)):
                if i != index:
                    nums[i] = 0
            return nums
        else:
            for i in nums:
                sum *= i
            for i in nums:
                s.append(int(sum/i))
            return s