#qus:- Given a number N, the task is to find the largest prime factor of that number.
class Solution:
    def largestPrimeFactor(self, N):
        largest_factor = 2
        while N > 1:
            if N % largest_factor == 0:
                N //= largest_factor
            else:
                largest_factor += 1
        return largest_factor
    
solution = Solution()
N = 21212
print(solution.largestPrimeFactor(N))