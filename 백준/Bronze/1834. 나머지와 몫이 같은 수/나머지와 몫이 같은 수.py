from sys import stdin
input = stdin.readline
def find_answer(number):
    answer = 0
    for i in range(1, number):
        answer += (i*number)+i
    return answer

print(find_answer(int(input())))