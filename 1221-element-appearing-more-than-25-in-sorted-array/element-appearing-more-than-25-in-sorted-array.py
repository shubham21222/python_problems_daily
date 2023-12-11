class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0
        if not arr:
            return 1
        target = len(arr) // 4 + 1
        for i in range(0,len(arr)):
                if arr[i]==arr[i+target - 1]:
                    return arr[i]

        