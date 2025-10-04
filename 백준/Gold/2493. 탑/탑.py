from sys import stdin
input = stdin.readline
from collections import deque
def main():
    t_count = int(input().strip())
    tower_list = list(map(int, input().split()))
    que = deque()
    answer = list()
    que.append((tower_list[0], 0))
    answer.append(0)
    for i in range(1, t_count):
        while que and que[-1][0] <= tower_list[i]:
            que.pop()
        if que:
            answer.append(que[-1][1]+1)
        else:
            answer.append(0)
        que.append((tower_list[i], i))
    print(*answer)
    return
if __name__ == "__main__":
    main()