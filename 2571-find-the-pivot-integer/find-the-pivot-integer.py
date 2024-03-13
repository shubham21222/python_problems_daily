class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_of_numbers = n * (n + 1) // 2
        square_root = int(sum_of_numbers ** 0.5)
        if sum_of_numbers == square_root * square_root:
            return square_root
        else:
            return -1 
