class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        played=set()
        losses=collections.Counter()
        for winner,loser in matches:
            played.add(winner)
            played.add(loser)
            losses[loser]+=1
        ans=[[],[]]
        for player in sorted(played):
            if losses[player]==0:
                ans[0].append(player)
            if losses[player]==1:
                ans[1].append(player)
        return ans
        