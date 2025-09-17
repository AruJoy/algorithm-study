from sys import stdin
input = stdin.readline

def get_input():
    target = int(input().strip())
    broken_count = int(input().strip()) 
    key_list = [i for i in range(10)]
    if broken_count>0:
        broken_key_list = list(map(int, input().split(" ")))
        broken_key_list.sort(reverse=True)
        for key in broken_key_list:
            key_list.pop(key)
    numbers = 1 if target == 0 else len(str(abs(target)))
    return target, key_list, 10-broken_count, numbers

def get_push_count(target, key_list, key_count, numbers ,current_value ,depth):
    now = 100
    target/10
    value = current_value
    answer = abs(target - now)
    for i in range(key_count):
        add_value = key_list[i] * (10**depth)
        value += add_value
        answer = min(abs(value - target) + depth+1, answer)
        if depth < numbers:
            answer = min(answer, get_push_count(target, key_list, key_count, numbers, value , depth+1))
        value -= add_value
    return answer

target, key_list, key_count, numbers = get_input()
print(get_push_count(target, key_list, key_count, numbers, 0, 0))