from sys import stdin

def sort(a):
    a = a.sort()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                a.remove(j)
    
numberOfSize = int(stdin.readline())
inputList = list()
for i in range(numberOfSize):
    inputList.append(stdin.readline())
sort(inputList)
