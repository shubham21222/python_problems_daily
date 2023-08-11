#qus :- Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
#Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize dp array with a maximum value initially
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1
