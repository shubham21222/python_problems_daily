class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = [bit for bit in s]
        low = 0
        high = len(s)-1
        for i in range(len(s)):
            if s[i] == '1':
                s[i],s[low] = s[low],s[i]
                low += 1

        s[low-1], s[high] = s[high] , s[low-1]
        return "".join(s)