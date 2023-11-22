class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_set = set(nums)

        result = []
        for i in range(1, len(nums) + 1):
            if i not in new_set:
                result.append(i)

        return result
