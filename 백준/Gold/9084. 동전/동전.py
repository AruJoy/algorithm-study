from sys import stdin
def coin (prices, coins):
    coin_combinations = dict()
    coin_combinations[0] = [0 for _ in range(prices + 1)]
    for coin in range(0, len(coins)):
        before_coin_condition = coin_combinations[coin]
        current_coin_condition = [0 for _ in range(prices + 1)]
        current_coin_condition[0] = 1
        for price in range(1, prices+1):
            if coins[coin] <= price:
                current_coin_condition[price] = (before_coin_condition[price] + 
                                                current_coin_condition[price - coins[coin]])
            else: current_coin_condition[price] = before_coin_condition[price]
        coin_combinations[coin+1] = current_coin_condition

    return coin_combinations[len(coins)][prices]

test_times = int(stdin.readline())

for test in range(test_times):
    coin_types = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    price = int(stdin.readline())
    
    print(coin(price, coins))