#qus:- Given two strings, find the length of longest subsequence present in both of them. Both the strings are in uppercase latin alphabets.


class Solution:
    
    # Function to find the length of longest common subsequence in two strings.
    def lcs(self, x, y, s1, s2):
        m, n = len(s1), len(s2)
        
        # Create a 2D DP table to store the length of LCS.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Return the length of LCS.
        return dp[m][n]
sol = Solution()
x= "AHJGHDAJ"
y= "ASDSAASJN"
result = sol.lcs(x,y,len(x),len(y))
print("length of LCS: ",result)