class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s.split()
        new_word = new_str[-1]
        return len(new_word)