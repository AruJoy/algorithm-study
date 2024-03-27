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
treeList.sort(reverse=True)

def isMeetTheCondition(n,value,a):
    sqr = sumOfTreeLength - ((n+1) * value)
    gotTree = sqr - sum(a[n+1:])
    if targetLength <= gotTree:
        return True
    else:
        return False
    
checkpoint = 0
for i in range(len(treeList)):
    length = treeList[i]
    if isMeetTheCondition(i, length, treeList):
        checkpoint = i
        break
    checkpoint = i
    checkpointLength = treeList[checkpoint]
for i in range(treeList[checkpoint], treeList[checkpoint-1]):
    if not isMeetTheCondition(checkpoint-1, i, treeList):
        print(i - 1)
        break