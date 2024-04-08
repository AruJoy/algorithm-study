from sys import stdin
def coin(coins, price):
    count = 0
    for coin in coins:
        count += price//coin
        price = price - (price//coin)*coin
        if price == 0: break
    return count

n_coin, price = map(int, stdin.readline().split(' '))
coins = list()
for _ in range(n_coin):
    coins.append(int(stdin.readline()))
coins.reverse()
print(coin(coins, price))