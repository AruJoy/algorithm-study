from sys import stdin
def fivo (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fivo = dict()
    for _ in range(n+1):
        fivo[_] = -(10**9)
    fivo[0] = 0
    fivo[1] = 1
    fivo[2] = 1
    if n > 1:
        for i in range(2, n+1):
            fivo[i] = fivo[i-1] + fivo[i-2]
        return fivo[n]

n = int(stdin.readline())
print(fivo(n))