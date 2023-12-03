class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        n = len(points)

        for i in range(n-1):
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[i+1][0], points[i+1][1]
            time += max(abs(x2-x1), abs(y2-y1))
        
        return time

