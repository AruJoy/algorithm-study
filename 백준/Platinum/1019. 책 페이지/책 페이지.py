from sys import stdin
input = stdin.readline
def main():
    number_str = input().strip()
    number = int(number_str)
    number_list = list(map(int, number_str))
    number_list.reverse()
    length = len(number_list)
    answer = []
    count = 0
    for j in range(length):
        count += ((number//10**(j+1))*10**j) - 10**j
        if j != length-1 and number_list[j] > 0:
            count += 10**j
        if j != length-1 and number_list[j] == 0:
            count += number % (10**j) + 1
    count += 10**(length-1)
    answer.append(count)
    for i in range(1,10):
        count = 0
        for j in range(length):
            count += (number//10**(j+1))*10**j
            if number_list[j] > i:
                count += 10**j
            if number_list[j] == i:
                count += number % (10**j) + 1
        answer.append(count)
    print(*answer)
    return
if __name__ == "__main__":
    main()