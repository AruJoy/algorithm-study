from sys import stdin

input = stdin.readline()
input = input.split(' ')
numberOfTrees = int(input[0])
targetLength = int(input[1])
treeList = stdin.readline()
treeList = treeList.split(' ')

for i in range(len(treeList)):
    treeList[i] = int(treeList[i])

sumOfTreeLength = sum(treeList) 

def isMeetTheCondition(value,a):
    gotLength = sum(max(0, i-value) for i in a)
    return gotLength>=targetLength

def pickTree(treeList):
    left = 0
    right = max(treeList)
    result = 0
    while left <= right:
        mid = (left + right) // 2

        if isMeetTheCondition(mid, treeList):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

print(pickTree(treeList))