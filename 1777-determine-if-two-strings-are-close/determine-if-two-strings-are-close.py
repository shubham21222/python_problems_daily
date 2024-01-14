class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        count_word1 = [word1.count(char) for char in set(word1)]
        count_word2 = [word2.count(char) for char in set(word2)]

        return sorted(count_word1) == sorted(count_word2)

         