class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([m[::-1] for m in s.split(" ")])
        