from sys import stdin
num_input = int(stdin.readline())
def fac(n):
    if n<=1:
        return 1
    return fac(n-1) * n

print(fac(num_input))