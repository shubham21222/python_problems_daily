class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        curr=bank[-1].count('1')
        nextt=0
        i=len(bank)-2
        cnt=0
        while i>=0:
            nextt=bank[i].count('1')
            if nextt==0:
                i-=1
                continue
            else:
                cnt+=nextt*curr
                curr=nextt
                nextt=0
            i-=1
        return cnt