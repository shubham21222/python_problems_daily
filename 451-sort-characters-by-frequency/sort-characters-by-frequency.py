class Solution:
    def frequencySort(self, s: str) -> str:
        f = []
        for i in set(s):
            f.append([s.count(i) , i])
        res = ''
        f.sort()
        print(f)
        for i in f[::-1]:
            res += str(i[1] * i[0])
        return res