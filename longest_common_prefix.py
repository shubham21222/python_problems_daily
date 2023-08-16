#qus:- Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string in the array
        shortest_str = min(strs, key=len)
        
        for i, char in enumerate(shortest_str):
            for other_str in strs:
                if other_str[i] != char:
                    return shortest_str[:i]
        
        return shortest_str