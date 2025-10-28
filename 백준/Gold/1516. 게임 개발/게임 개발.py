
from sys import stdin
from collections import deque
input = stdin.readline


def solution(n_tower, degree_table, time_table):
    ans = [0 for _ in range(n_tower)]
    que = deque()
    max_times = [0 for _ in range(n_tower)]
    for i in range(n_tower):
        if degree_table[i][0] != 0:
            continue

        que.append((i, 0))
        while que:
            tower, cur_time = que.popleft()
            time_table
            cur_time = max(max_times[tower], cur_time) + time_table[tower]
            ans[tower] = cur_time
            degree_table[tower][0] -= 1

            for child in degree_table[tower][1]:
                degree_table[child][0] -= 1

                if degree_table[child][0] == 0:
                    que.append((child, cur_time))
                    continue
                max_times[child] = max(max_times[child], cur_time)
    return ans


def main():
    n_tower = int(input().strip())
    degree_table = [[0, list()] for _ in range(n_tower)]
    time_table = list()
    for i in range(n_tower):
        line = list(map(int, input().split()))
        time_table.append(line[0])
        for j in range(1, len(line)):
            if line[j] == -1:
                break
            parent = line[j] - 1
            degree_table[parent][1].append(i)
            degree_table[i][0] += 1
    ans_list = solution(n_tower, degree_table, time_table)
    for ans in ans_list:
        print(ans)
    return


if __name__ == "__main__":
    main()
