from sys import stdin
def fivo (n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    fivo = list()
    fivo.append(0)
    fivo.append(1)
    fivo.append(2)
    if n > 2:
        for i in range(3, n+1):
            fivo.append((fivo[i-1] + fivo[i-2])% 15746)
    return fivo[n]

n = int(stdin.readline())
print(fivo(n))