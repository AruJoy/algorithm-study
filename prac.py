from sys import stdin
import math

def find_min_max(numbers, numbers_list, operator, arithmetic, minimum, maximum):
    if len(operator) == numbers-1:
        if operator[0] == 0:
            result = int(number_list[0] + number_list[1])
        elif operator[0] == 1:
            result = int(number_list[0] - number_list[1])
        elif operator[0] == 2:
            result = int(number_list[0] * number_list[1])
        elif operator[0] == 3:
            result = int(number_list[0] / number_list[1])
        for i in range(1, len(operator)):
            if operator[i] == 0:
                result = int(result + number_list[i+1])
            elif operator[i] == 1:
                result = int(result - number_list[i+1])
            elif operator[i] == 2:
                result = int(result * number_list[i+1])
            elif operator[i] == 3:
                result = int(result / number_list[i+1])
        minimum = min(minimum, int(result))
        maximum = max(maximum, int(result))
        return[minimum, maximum]
    
    
    for i in range(4):
        temp_ari = arithmetic.copy()
        temp_oper = operator.copy()
        if arithmetic[i] != 0:
            operator.append(i)
            arithmetic[i] -= 1
            minimum, maximum = find_min_max(numbers, numbers_list, operator, arithmetic, minimum, maximum)
        arithmetic = temp_ari
        operator = temp_oper
    return[minimum, maximum]

numbers = int(stdin.readline())
number_list = list(map(int, stdin.readline().strip().split(' ')))
arithmetic = list(map(int, stdin.readline().strip().split(' ')))

minimum, maximum = find_min_max(numbers, number_list, list(), arithmetic, 1e10, -1e10)
print(maximum)
print(minimum)