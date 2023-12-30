class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = {}

        for word in words:
            for char in word:
                if char in char_count:
                    char_count[char] += 1

                else:
                    char_count[char] = 1

        for count in char_count.values():
            if count % len(words) != 0:
                return False
    
        return True