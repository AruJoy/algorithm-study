from sys import stdin
import sys
sys.setrecursionlimit(10000)
input = stdin.readline
INF = float("INF")
def get_cost(house_count, color_cost, house_list, dp):
    if len(house_list) == house_count: return 0
    if house_list and dp[house_list[-1]][len(house_list)-1] != -1:
        return dp[house_list[-1]][len(house_list)-1]
    min_cost = INF
    for i in range(3):
        if house_list and house_list[-1] == i :
            continue
        color = color_cost[len(house_list)][i]
        house_list.append(i)
        cost = get_cost(house_count, color_cost, house_list, dp)
        min_cost = min(min_cost, color + cost)
        house_list.pop()
    if house_list:
        dp[house_list[-1]][len(house_list)-1] = min_cost
    return min_cost
def main():
    house_count = int(input().strip())
    color_cost = []
    house_list = []
    dp = [[-1 for _ in range(house_count)] for i in range(3)]
    for _ in range(house_count):
        color_cost.append(list(map(int, input().split())))
    print(get_cost(house_count, color_cost, house_list, dp))
    return
if __name__ == "__main__":
    main()