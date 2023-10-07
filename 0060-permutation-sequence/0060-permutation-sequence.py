class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1 
        result = []
        nums = list(range(1, n + 1))

        for i in range(n):
            index = k // factorial[n - 1 - i]
            result.append(str(nums.pop(index)))
            k %= factorial[n - 1 - i]

        return ''.join(result)