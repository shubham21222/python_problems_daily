class Solution:
    def countSubstrings(self, s: str) -> int:
        new_str = []
        for i in range(len(s)+1):
            for j in range(i):
                new_str.append(s[j:i])

        count = 0
        for i in new_str:
            if i==i[::-1]:
                count += 1

        return count