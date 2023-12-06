class Solution:
    def totalMoney(self, n: int) -> int:
        sum_num = 0

        for i in range(n):
            sum_num += i//7+1+(i%7)


        return sum_num 