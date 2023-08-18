#qus:- Given an integer x, return true if x is a  palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

    def check_palindrome(self):
        n = int(input("Enter a number: "))
        s = self.isPalindrome(n)
        print(s)
