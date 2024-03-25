from sys import stdin
count = 0
moves = list()
def hanoi(n, start, sub, target, count):
    if n == 1:
        count = moves.append([start, target])
        return count + 1
    hanoi(n-1, start, target, sub, count)
    moves.append([start, target])
    count = count +1
    hanoi(n-1, sub, target, start, count)
    
n = int(stdin.readline())

hanoi(n, 1, 2, 3, 0)
print(count)
for move in moves:
    print(f'{move[0]} {move[1]}')