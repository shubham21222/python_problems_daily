class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i , j , ans = 0,0,0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                j += 1
                i += 1
                ans += 1
            else:
                j+= 1
        return ans
        
