from sys import stdin
input = stdin.readline
from collections import deque

def main():
    n_car = int(input().strip())
    init = list()
    result = list()
    for _ in range(n_car):
        init.append(input().strip())
    for _ in range(n_car):
        result.append(input().strip())
    i = 0
    j = 0
    ans = 0
    while i < len(init) and j < n_car:
        if init[i] == result[j]:
            i += 1
            j += 1
            continue
        if init[i] != result[j]:
            ans += 1
            init.remove(result[j])
            j += 1
            continue
    print(ans)
    return
if __name__ == "__main__":
    main()