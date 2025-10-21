from sys import stdin
from collections import deque
input = stdin.readline

MOD = 10000
POW = 1000


def bfs(target, value, result, que, visited_list, char):
    if not (0 <= result <= MOD):
        return False
    if visited_list[result][0]:
        return False
    visited_list[result][0] = True
    visited_list[result][1] = value
    visited_list[result][2] = char
    if result == target:
        return True
    que.append(result)
    return False


def double(target, value, que, visited_list):
    result = value * 2
    result = result % MOD if result >= MOD else result
    return bfs(target, value, result, que, visited_list, "D")


def sub(target, value, que, visited_list):
    result = 9999 if value == 0 else value - 1
    return bfs(target, value, result, que, visited_list, "S")


def rotate_l(target, value, que, visited_list):
    result = (value % POW) * 10 + (value // POW)
    return bfs(target, value, result, que, visited_list, "L")


def rotate_r(target, value, que, visited_list):
    result = (value % 10) * POW + (value // 10)
    return bfs(target, value, result, que, visited_list, "R")


def find_path(start, target):
    visited_list = [[False, -1, ""]for _ in range(10001)]
    que = deque()
    visited_list[start][0] = True
    que.append(start)
    while que:
        current = que.popleft()
        if double(target, current, que, visited_list):
            break
        if sub(target, current, que, visited_list):
            break
        if rotate_l(target, current, que, visited_list):
            break
        if rotate_r(target, current, que, visited_list):
            break
    cur = target
    ans = []
    while (visited_list[cur][1] >= 0):
        ans.append(visited_list[cur][2])
        cur = visited_list[cur][1]
    ans = "".join(reversed(ans))
    return ans


def main():
    n_test = int(input().strip())
    for _ in range(n_test):
        start, target = map(int, input().split())
        print(find_path(start, target))
    return


if __name__ == "__main__":
    main()
