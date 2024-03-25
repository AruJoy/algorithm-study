from sys import stdin
n = int(stdin.readline())
def hanoi(n, start, sub, target):
    if n == 1:
        print(f'{start} {target}')
        return
    hanoi(n-1, start, target, sub)
    print(f'{start} {target}')
    hanoi(n-1, sub, start, target)
sqr = 2**n
print(f'{sqr - 1}')
if n < 21 :
    hanoi(n, 1, 2, 3)