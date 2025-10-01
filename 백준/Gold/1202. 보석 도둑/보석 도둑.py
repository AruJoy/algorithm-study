from sys import stdin
from heapq import heappop, heappush
input = stdin.readline
MOD = 1000000007
def main():
    n_stone, n_bag = map(int, input().split())
    stone_list = list()
    bag_list = list()
    for _ in range(n_stone):
        weight, valuation = map(int, input().split())
        stone_list.append((weight, valuation))
    for _ in range(n_bag):
        bag_list.append(int(input().strip()))
    stone_list.sort()
    bag_list.sort(reverse = True)
    value = list()
    ans = 0
    i = 0
    while i <= n_stone:
        if not bag_list:
            break
        if i < n_stone and stone_list[i][0] <= bag_list[-1]:
            heappush(value, (-stone_list[i][1]))
            i += 1
            continue
        if value:
            ans -= heappop(value)
        bag_list.pop()
    print(ans)
    return

if __name__ == "__main__":
    main()