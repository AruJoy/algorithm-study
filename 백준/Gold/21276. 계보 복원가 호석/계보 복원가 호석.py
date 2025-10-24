from sys import stdin
from collections import deque
input = stdin.readline


def find(union, cur):
    if cur == union[cur]:
        return cur
    union[cur] = find(union, union[cur])
    return union[cur]


def get_answer(names, degree_map):
    answer_map = dict()
    ancients = list()
    for name in names:
        if degree_map[name][0] == 0:
            ancients.append(name)
            que = deque()
            que.append(name)
            while que:
                cur = que.popleft()
                answer_map[cur] = list()
                degree_map[cur][0] -= 1
                for nxt in degree_map[cur][1]:
                    degree_map[nxt][0] -= 1
                    if degree_map[nxt][0] == 0:
                        answer_map[cur].append(nxt)
                        if len(degree_map[nxt][1]) == 0:
                            degree_map[nxt][0] -= 1
                            continue
                        que.append(nxt)
    print(len(ancients))
    print(*ancients)
    for name in names:
        if name in answer_map:
            answer_map[name].sort()
            print(name +
                  " " +
                  str(len(answer_map[name])) + " " +
                  " ".join(answer_map[name]))
            continue
        print(name + " 0")
    return


def main():
    n_name = int(input().strip())
    names = list(input().split())
    names.sort()
    n_count = int(input().strip())
    degree_map = dict()
    for name in names:
        degree_map[name] = [0, list()]
    for _ in range(n_count):
        child, parent = input().split()
        degree_map[child][0] += 1
        degree_map[parent][1].append(child)
    get_answer(names, degree_map)
    return


if __name__ == "__main__":
    main()
