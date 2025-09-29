from sys import stdin
input = stdin.readline
INF = float('INF')
def promote(target, n_city, cost_sheet):
    dp = [[INF for _ in range(target+1)] for __ in range (n_city)]
    for i in range(n_city):
        dp[i][0] = 0
    _, people, cost = cost_sheet[0]
    for j in range(1, target+1):
        dp[0][j] = ((j - 1) // people + 1) * cost
    for i in range(1, n_city):
        _, people, cost = cost_sheet[i]
        for j in range(1, target+1):
            before_j = max(0, j - people)
            dp[i][j] = min(dp[i-1][j], dp[i][before_j]+ cost)
    return dp[n_city-1][target]

def main():
    target, n_city = map(int, input().split())
    cost_sheet = []
    for i in range(n_city):
        cost, gain_people = map(int, input().split())
        cost_sheet.append((cost/gain_people, gain_people, cost))
    cost_sheet.sort()
    print(promote(target, n_city, cost_sheet))
    return

if __name__ == "__main__":
    main()
