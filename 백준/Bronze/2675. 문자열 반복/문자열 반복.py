from sys import stdin
input = stdin.readline()
input = int(input)
inputList = list()
for i in range(input):
    inputList.append(stdin.readline())
for i in inputList:
    splited = i.split(' ')
    splited[1] = splited[1].replace('\n', '')
    for k in splited[1]:
        print( k * int(splited[0]), end ='')
    print()