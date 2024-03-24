n = int(input('자료수를 입력하세요.: '))
inputList = []

for i in range(n):
    value = int(input(f'{i+1} 번째 값을 입력하세요.: '))
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
        if a[n] >= listUpList[i]:
            listUpList.insert(i,a[n])
            return
    listUpList.append(a[n])

def listUp2(a, n, listUpList):
    #=============선언조건 명시===========
    if n == 0:
        listUpList.append(a[n])
        return
    listUp2(a, n-1, listUpList)  # 재귀 호출: 리스트의 이전 값들을 정렬

    #===============탈출 명시 ==========
    if len(a) == len(listUpList):  # 탈출 조건: 리스트가 정확히 정렬됨
        return listUpList
    
    #=============== 진행 명시 =========
    for i in range(len(listUpList)):  # 진행 조건: 리스트를 순회하며 적절한 위치를 찾음
        if a[n] >= listUpList[i]:
            listUpList.insert(i, a[n])  # 적절한 위치에 값을 삽입하고 함수 종료
            return
    listUpList.append(a[n])  # 삽입할 위치를 찾지 못한 경우, 리스트의 맨 끝에 값을 추가

print(inputList)

def mySort(inputList):
    oldList = inputList.copy()
    for i in range(len(inputList) - 1):
        print(f"i = {i}")
        if inputList[i] > inputList[i + 1]:
            bigger = inputList[i]
            inputList[i] = inputList[i + 1]
            inputList [i + 1] = bigger
            print("change!: ", end="")
            print(inputList)
        else:
            print("no change: ", end="")
            print(inputList)
    print("oldList is ", end="")
    print(oldList)
    print("now numList is ", end="")
    print(inputList)
    if oldList == inputList:
        print("----------끝----------")
        print(inputList)
        return
    print("----------다시----------")
    mySort(inputList)

def mySort(inputList, n):
    if n < 0:
        return inputList
    inputList = mySort(inputList, n-1)
    
    print("oldList is ", end="")
    print(inputList)
    
    for i in range(n):
        print(f"i = {i}")
        if inputList[i] < inputList[i + 1]:
            smaller = inputList[i]
            inputList[i] = inputList[i + 1]
            inputList [i + 1] = smaller
            print("change!: ", end="")
            print(inputList)
            return inputList
        else:
            print("no change: ", end="")
            print(inputList)
    
    return inputList


print(mySort(inputList, len(inputList)-1))


listUp(inputList, n)
print(listUpList)

listUpList = []
listUp2(inputList, n-1, listUpList)
print(listUpList)