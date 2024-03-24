from sys import stdin
input = list()
for i in range(9):
    input.append(int(stdin.readline()))

biggest = list([0, 0])
for i in range(9):
    if biggest[1]< input[i]:
        biggest[0] = i+1
        biggest[1] = input[i]
print(biggest[1])
print(biggest[0])