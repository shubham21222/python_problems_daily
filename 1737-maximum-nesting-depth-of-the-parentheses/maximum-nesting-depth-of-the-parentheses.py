class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        max_count = 0
        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
                max_count = max(max_count,counter)
            elif s[i]==")":
                if counter > 0: 
                    counter -= 1
                else:
                    return -1
        return max_count
        