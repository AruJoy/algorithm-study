from sys import stdin
input = stdin.readline()
input = int(input)
inputList = list()
inputList = stdin.readline().split(' ')
for i in range(input):
    inputList[i] = int(inputList[i])

count = 0
for i in inputList:
    if i == 2:
        count = count + 1
    for j in range(2,i):
        if i%j == 0:
            break
        if j == i-1:
            count = count + 1
            break

print(count)