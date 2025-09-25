from sys import stdin
from collections import deque
input = stdin.readline

def do_puzzle(puzzle, index):
    if puzzle == ("123456780"):
        return 0
    visited_list = set()
    visited_list.add(puzzle)
    que = deque()
    que.append((puzzle, index, 0))
    dx = [-3, 3, -1, 1]
    dx1 = [-3, 3, -1]
    dx2 = [-3, 3, 1]
    while que:
        cur_p, cur_i, cur_m = que.popleft()
        cur_dx = dx
        if cur_i%3 == 0:
            cur_dx = dx2
        if cur_i%3 == 2:
            cur_dx = dx1
        
        for d in cur_dx:
            i = cur_i + d
            if(0<= i <= 8):
                if i < cur_i:
                    copy_p = cur_p[:i]+ cur_p[cur_i] + cur_p[i+1 : cur_i] + cur_p[i]+ cur_p[cur_i+1:]
                else:
                    copy_p = cur_p[:cur_i]+ cur_p[i] + cur_p[cur_i+1 : i] + cur_p[cur_i]+ cur_p[i+1:]
                if not copy_p in visited_list:
                    if copy_p == "123456780":
                        return cur_m + 1
                    visited_list.add(copy_p)
                    que.append((copy_p, i, cur_m+1))
    return -1

def main():
    puzzle = ""
    for _ in range(3):
        puzzle = puzzle + input().strip().replace(" ", "")
    for i in range(9):
        if puzzle[i] == "0":
            break
    print(do_puzzle(puzzle, i))
    return
if __name__ == "__main__":
    main()