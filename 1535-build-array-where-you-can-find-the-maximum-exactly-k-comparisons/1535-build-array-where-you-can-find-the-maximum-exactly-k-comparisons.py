class Solution:
    MOD = 10**9 + 7

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        visited = {}

        def dp(i, biggest, cost):
            if i == n:
                return cost == k
            if cost > k or k - cost > m - biggest or k - cost > n - i:
                return 0
            if (i, biggest, cost) in visited:
                return visited[(i, biggest, cost)]

            res = 0
            for val in range(1, m + 1):
                res = (res + dp(i + 1, max(biggest, val), cost if val <= biggest else cost + 1)) % self.MOD

            visited[(i, biggest, cost)] = res
            return res

        return dp(0, 0, 0)