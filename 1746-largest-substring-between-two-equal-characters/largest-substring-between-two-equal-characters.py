class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max=-1
        for i in range(len(s)):
            for j in range(i,len(s)):
                if(s[i]==s[j] and j-i>max):
                    max=j-i
        return max-1            
        