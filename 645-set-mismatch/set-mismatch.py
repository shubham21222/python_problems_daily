class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sum_nums = len(nums)*(len(nums)+1)//2
        repetition = sum(nums) - sum(set(nums))
        loss = sum_nums - sum(set(nums))
        return [repetition,loss]