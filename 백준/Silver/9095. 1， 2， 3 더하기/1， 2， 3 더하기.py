from sys import stdin

def get_input():
    number_count = int(input().strip())
    number_dp = [-1 for i in range(11)]
    number_list = []
    for _ in range(number_count):
        number_list.append(int(input().strip()))
    return number_dp, number_list
def find_combination(number, before_number):
    if number == before_number:
        return 1
    if number < before_number:
        return 0
    count = 0
    for i in range(1, 4):
        count += find_combination(number, before_number + i)
    return count
def solution(number_dp, number_list):
    for number in number_list:
        if number_dp[number] != -1:
            print(number_dp[number])
            continue
        number_dp[number] = find_combination(number, 0)
        print(number_dp[number])
    return
number_dp, number_list = get_input()
solution(number_dp, number_list)