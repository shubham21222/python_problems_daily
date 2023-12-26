class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        ans = 0
        MOD = 10**9 + 7
        @cache
        def recursive(n,target):
            nonlocal ans
            if n==0:
                if target==0:
                    return 1 
                else:
                    return 0
            subans = 0
            for i in range(1,min(target,k)+1):
                subans += recursive(n-1, target-i)
                subans %= MOD
            return subans
        ans = recursive(n, target)
        return ans
                
