from sys import stdin
from math import sqrt
def factorization(num):
    number = num
    factor_list = list()
    while number != 1:
        for i in range(2, number+1):
            if number % i == 0:
                factor_list.append(i)
                number = number//i
                break
    for i in range(len(factor_list)):
        print(factor_list[i])
    return

num = int(stdin.readline())
factorization(num)