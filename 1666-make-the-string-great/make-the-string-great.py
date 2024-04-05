class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return s

        i = 0
        while i < len(s) - 1:
            if s[i] != s[i + 1] and s[i].lower() == s[i + 1].lower():
                s = s[:i] + s[i + 2:]
                i = 0
            else:
                i += 1

        return s
