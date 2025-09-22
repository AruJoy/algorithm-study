from sys import stdin
input = stdin.readline
from collections import deque
def init():
    target = int(input().strip())
    bfs_table = [[ -1 for _ in range(target*2+1) ] for __ in range(target*2+1) ]
    return target, bfs_table

def get_solution(target, bfs_table):
    answer = float("INF")
    Max = target*2
    bfs_table[1][0] = 0
    que = deque()
    que.append((1, 0, 0))
    
    while que:
        value, paste, count = que.popleft()
        
        if value == target:
            return count
        
        if bfs_table[value][value] == -1 and 0 < value:
            bfs_table[value][value] = count +1
            que.append((value, value, count + 1))
        
        if 0 < paste and value + paste <= Max and bfs_table[value + paste][paste] == -1:
            bfs_table[value + paste][paste] = count +1
            que.append((value + paste, paste, count +1))
        
        if 0 < value and bfs_table[value - 1][paste] == -1:
            bfs_table[value - 1][paste] = count +1
            que.append((value - 1, paste, count + 1))
    
    return answer
target, bfs_table = init()

print(get_solution(target, bfs_table))