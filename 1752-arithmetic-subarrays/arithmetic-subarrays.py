from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        
        for i in range(len(r)):
            left = l[i]
            right = r[i]

            
            sub_array = nums[left:right+1]

            is_arithmetic = True 

            if len(sub_array) > 2:
                sub_array.sort()
                diff = sub_array[1] - sub_array[0]

                for j in range(2, len(sub_array)):
                    if sub_array[j] - sub_array[j-1] != diff:
                        is_arithmetic = False
                        break 

            result.append(is_arithmetic)

        return result
