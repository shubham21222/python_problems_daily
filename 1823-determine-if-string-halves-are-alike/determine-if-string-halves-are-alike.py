class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowles = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        first_half = s[:len(s)//2]
        second_half = s[len(s)//2:]
        count_a = 0
        count_b = 0
        for i in first_half:
            if i in vowles:
                count_a += 1

        for j in second_half:
            if  j in vowles:
                count_b += 1

        if count_a == count_b:
            return True

        else:
            return False

        