class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = defaultdict(int)
        for num in arr:
            m[num] += 1

        s= set()
        for cnt in m.values():
            s.add(cnt)

        return len(s) == len(m)
        