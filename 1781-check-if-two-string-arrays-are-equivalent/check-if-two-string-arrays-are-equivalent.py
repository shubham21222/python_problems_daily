class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_result = ''.join(word1)
        word2_result = ''.join(word2)
        
        
        is_equivalent = word1_result == word2_result

        return is_equivalent 