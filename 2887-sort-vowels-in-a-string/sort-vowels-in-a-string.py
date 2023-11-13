class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        # Extract consonants and vowels from the string
        consonants = [char for char in s if char not in vowels]
        vowels_list = [char for char in s if char in vowels]

        # Sort vowels based on their ASCII values
        sorted_vowels = sorted(vowels_list, key=ord)

        # Reconstruct the final string with sorted vowels and original consonants
        final_string = []
        vowel_index = 0

        for char in s:
            if char in vowels:
                final_string.append(sorted_vowels[vowel_index])
                vowel_index += 1
            else:
                final_string.append(char)

        return ''.join(final_string)
