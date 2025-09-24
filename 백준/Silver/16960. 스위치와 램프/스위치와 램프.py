from sys import stdin
import sys
sys.setrecursionlimit(10000)
input = stdin.readline

def main():
    s_count, l_count = map(int, input().split())
    s_list = []
    for _ in range(s_count):
        str = input().strip()
        if len(str) == 1:
            s_list.append(set())
            continue
        s_list.append(set(list(map(int, str.split()))[1:]))
    for i in range(s_count):
        new_set = set()
        for j in range(s_count):
            if i == j: continue
            new_set.update(s_list[j])
            if len(new_set) == l_count:
                print(1)
                return
    print(0)
    return
if __name__ == "__main__":
    main()