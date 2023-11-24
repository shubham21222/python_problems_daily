class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sort_arr = sorted(piles,reverse=True)

        bob_coin = 0

        for i in range(1,len(sort_arr) // 3*2,2):
            
            bob_coin += sort_arr[i]

        return bob_coin 