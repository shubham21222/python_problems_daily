class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if  x >= 0   else -1
          

        new_str = str(abs(x))
        new_str2 = new_str[::-1]

        result = sign * int(new_str2)
        if result < -2**31 or result > 2**31 - 1:
            return 0


        return result