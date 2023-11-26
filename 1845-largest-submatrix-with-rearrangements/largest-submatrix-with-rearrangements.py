class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])


        counts = [[0] * n for _ in range(m)]

        for j in  range(n):
            for i in  range(m-1,-1,-1):
                if matrix[i][j]:
                    counts[i][j] = 1
                    if i<m-1:
                        counts[i][j] += counts[i+1][j]

        ans = 0
        for i in range(m):
            sortedCount = sorted(counts[i],reverse=True) 
            for j in range(n):
                ans = max(ans,sortedCount[j]*(j+1))


        return ans