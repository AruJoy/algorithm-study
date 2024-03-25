from sys import stdin
def quick(a, left, right):
    pivot = a[(left + right) // 2]
    pl = left
    pr = right
    while pl<=pr:
        while a[pl] < pivot:
            pl += 1
        while pivot < a[pr]:
            pr -= 1
        if pl<=pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    if left < pr:
        quick(a, left, pr)
    if pl < right:
        quick(a, pl, right)
    return

def qsort(a):
    quick(a, 0, len(a)-1)


numberOfSize = int(stdin.readline())
inputList = list()
for i in range(numberOfSize):
    inputList.append(int(stdin.readline()))

qsort(inputList)

for i in inputList:
    print(i)