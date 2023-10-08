class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        
        # Create a 2D DP table of size (m+1) x (n+1)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table using a bottom-up approach
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Calculate the dot product of subsequences ending at i and j
                dp[i][j] = max(nums1[i - 1] * nums2[j - 1], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], dp[i - 1][j], dp[i][j - 1])
        
        # The maximum dot product will be in dp[m][n]
        return dp[m][n]