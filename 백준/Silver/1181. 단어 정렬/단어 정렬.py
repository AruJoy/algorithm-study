from sys import stdin

numberOfSize = int(stdin.readline())
inputList = list()
for i in range(numberOfSize):
    inputList.append(stdin.readline())

inputList = list(set(inputList))
inputList.sort()
inputList.sort(key = len)


for i in inputList:
    print(i, end= '')