from sys import stdin
def knapsack(prices, weights, bag_capacity):
    knapsack_table = dict()
    knapsack_table[0] =  [0 for _ in range(bag_capacity+1)]
    for item in range(1, len(prices)):
        before_item_condition = knapsack_table[0]
        current_item_condition = [0 for _ in range(bag_capacity + 1)]
        for bag in range(1 , bag_capacity+1):
            before_item_condition = knapsack_table[item-1]
            if weights[item] <= bag:
                current_item_condition[bag] = max(before_item_condition[bag], before_item_condition[bag-weights[item]] + prices[item])
            else: current_item_condition[bag] = before_item_condition[bag]
        knapsack_table[item] = current_item_condition
    return knapsack_table[len(prices)-1][bag_capacity]

items, bag_capacity = map(int, stdin.readline().split(' '))
prices = [0]
weights = [0]
for item in range(items):
    weight, price = map(int, stdin.readline().split(' '))
    prices.append(price)
    weights.append(weight)
print(knapsack(prices, weights, bag_capacity))