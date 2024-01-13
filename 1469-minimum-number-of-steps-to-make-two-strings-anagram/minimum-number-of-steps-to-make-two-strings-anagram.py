class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sd,st= {},{}
        for i in s:
            if i in sd:
                sd[i]+= 1

            else:
                sd[i] = 1

        for i in t:
            if i in st:
                st[i] += 1
            else :
                st[i] = 1

        ans = 0
        for i in st:
            if i in sd:
                if st[i] > sd[i]:
                    ans += (st[i]-sd[i])

            else:
                ans += st[i]

        return ans