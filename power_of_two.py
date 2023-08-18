#qus:-#qus:- Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two, if there exists an integer x such that n == 2x.

def power(n):
    if n<=0:
        return False
    while n%2==0:
        n=n/2
    return n==1

#n = input(int("enter power :"))
s= power(512)
print(s)
