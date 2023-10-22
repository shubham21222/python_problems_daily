class Solution:
    def maximumScore(self, A, k):
        i = k - 1
        j = k + 1
        N = len(A)
        res = A[k]
        mn = A[k]
        while i >= 0 or j < N:
            if i < 0 or (j < N and A[j] > A[i]):
                mn = min(mn, A[j])
                j += 1
            else:
                mn = min(mn, A[i])
                i -= 1
            res = max(res, mn * (j - i - 1))
        return res