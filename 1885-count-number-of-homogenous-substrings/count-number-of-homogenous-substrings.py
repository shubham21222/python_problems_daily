class Solution:
    def countHomogenous(self, s):
        i = 0
        j = 1
        res = 0
        while i < len(s):
            while j < len(s) and s[j] == s[i]:
                j += 1
            n = j - i
            res += (n * (n+1)) // 2
            i = j
        return res % (10**9 + 7)