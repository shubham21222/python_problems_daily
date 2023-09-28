class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        result2 = []
        for num in nums:
            if num % 2 == 0:
                result.append(num)
            else: 
                result2.append(num)
        result.extend(result2)
        return result