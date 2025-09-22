from sys import stdin

def get_input():
    numbers = input().strip()
    return len(numbers), int(numbers)
def solution(length:int, number:int):
    new_number_length = 0
    for i in range(length):
        power = i
        if number >= 10**(power+1):
            dff = 10**(power)
            count = 10**(power+1)-dff
            new_number_length += count * (power + 1)
            continue
        count = number - 10**(power) +1
        new_number_length += count * (power + 1)
    return new_number_length
length, numbers = get_input()
print(solution(length, numbers))