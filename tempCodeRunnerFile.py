n = int(input())
inputList = []

for i in range(n):
    value = int(input())
    inputList.append(value)

listUpList = []

def listUp(a, n):
    global listUpList
    #=============선언조건 명시===========
    if n == 0:
        listUpList.append(a[n])
        return
    listUp(a, n-1)
    #===============탈출 명시 ==========
    if len(a) == len(listUpList):
        return
    #=============== 진행 명시 =========
    for i in range(len(listUpList)):
        if a[n] <= listUpList[i]:
            listUpList.insert(i,a[n])
            return
    listUpList.append(a[n])
    return
listUp(inputList, n)
for i in listUpList:
    print(i)