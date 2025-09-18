from sys import stdin
import sys
sys.setrecursionlimit(10**5)
input = stdin.readline

def get_input():
    numbers = int(input().strip())
    sequence = list(map(int, input().split(" ")))
    return numbers, sequence
def solution(numbers, sequence, sequence_map, depth, flag):
    if depth == numbers:
        if flag[0] == 1:
            print(" ".join(map(str, sequence)))
        flag[0] += 1
        return
    for i in range(sequence[depth], numbers+1):
        if flag[0] != 0 and (sequence_map[i-1] or i == 0):
            continue
        if not flag[0] == 0:
            sequence_map[i-1] = True
            sequence[depth] = i
        solution(numbers, sequence, sequence_map, depth+1, flag)
        if flag[0]>1:return
        sequence_map[i-1] = False
        sequence[depth] = 0
    if depth == 0 and flag[0] < 2:
        print(-1)
    return

numbers, sequence = get_input()
flag = [0]
sequence_map = [True for _ in range(1, numbers+1)]
solution(numbers, sequence, sequence_map, 0, flag)