class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        stairs = 1
        for i in range(n):
            count , stairs = stairs , count + stairs
        return stairs
        