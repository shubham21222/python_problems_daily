class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = []

        onesRow = [0] * m
        onesCol = [0] * n
        zerosRow = [0] * m
        zerosCol = [0] * n

        for i in range(m):
            for j in range(n):
                onesRow[i] += grid[i][j]
                onesCol[j] += grid[i][j]
                zerosRow[i] += 1 - grid[i][j]
                zerosCol[j] += 1 - grid[i][j]


        diff = [[onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j] for j in range(n)] for i in range(m)]

        return diff
