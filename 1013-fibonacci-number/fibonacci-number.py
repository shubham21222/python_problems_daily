class Solution:
    def fib(self, n: int) -> int:

        first_num = 0
        second_num = 1

        if n== 0:
            return first_num
        for i in range(2,n+1):
            result = first_num + second_num
            first_num = second_num
            second_num = result

        return second_num 

