from sys import stdin
def mergeSort(a):
    if len(a) <= 1:
        return a
    middlePoint = len(a)//2
    pl = 0
    pr = 0
    newList = list()
    leftList = mergeSort(a[:middlePoint])
    rightList = mergeSort(a[middlePoint:])
    while len(newList) < len(leftList) + len(rightList):
        if pr >= len(rightList):
            newList.append(leftList[pl])
            pl += 1
        elif pl >= len(leftList):
            newList.append(rightList[pr])
            pr += 1
        else:
            if leftList[pl] < rightList[pr]:
                newList.append(leftList[pl])
                pl += 1
            else: 
                newList.append(rightList[pr])
                pr += 1
    return newList

inputSize = int(stdin.readline())
inputList = list()

for i in range(inputSize):
    inputList.append(int(stdin.readline()))

saltedCaramel = mergeSort(inputList)
for i in saltedCaramel:
    print(i)