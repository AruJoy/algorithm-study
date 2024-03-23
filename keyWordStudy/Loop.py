#basic usage

def dividingLine():
    print('''
=====================================================================================
''')
    
def useOfLoop():
    
    for x in 'abc':
        print (x)
    
    for x in [1, 2, 3]:
        print (x)
    dividingLine()
    
    dictionary = {'one':1, 'two':2, 'three':3}
    for x in dictionary:
        print(x)
        print(dictionary[x])
    dividingLine()
    
    for [x, y] in [[1,2], [3,4], [5,6]]:
        print(x,y)
    dividingLine()
    
    for i in range(0, 10, 2):
        if i == 0:
            print("for(i=0; i<10; i+=2){")
            print(' sout(i);')
            print('}')
        print(i)
    dividingLine()
    
    for i in range(0, 10):
        if i == 0:
            print("for(i=0; i<10; i++){")
            print(' sout(i);')
            print('}')
        print(i)
    dividingLine()
    
    for i in range(10):
        if i == 0:
            print("for(i=0; i<10; i++){")
            print(' sout(i);')
            print('}')
        print(i)
    dividingLine()
    
    return

def multipleLoop():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                print(i, j, k)
    dividingLine()

def breakAndContinue():
    for i in range(3):
        if i ==1:
            continue
        print(i)
    dividingLine()
    
    for i in range(10):
        if i == 3:
            break
        print(i)
    dividingLine()
    
    return

def useElseInLoopFunction():
    for x in [1, 2, 3]:
        print(x)
    else:
        print("끝")
    dividingLine()
    
    for x in [1, 2, 3]:
        print(x)
        if x == 2:
            break
    else:
        print("끝")
    dividingLine()
    
    return

def loopFunctionInList():
    a = 'abcde'
    b = [val + 'k' for val in a]
    print(b)
    dividingLine()
    
    a = [1, 2, 3, 4, 5]
    b = [val * 5 for val in a]
    print(b)
    dividingLine()
    
    a = 'abcde'
    b = [val + 'k' for val in a if val == 'c']
    print(b)
    dividingLine()
    
    a = [1, 2, 3, 4, 5]
    b = [val *5 for val in a if val <3]
    
    a1 = [1, 2, 3]
    a2 = [6, 7, 8]
    b= [val1 + val2 for val1 in a1 if val1 < 3
                    for val2 in a2 if val2 < 7]
    print (b)
    dividingLine()
    
    return

useOfLoop()
multipleLoop()
breakAndContinue()
useElseInLoopFunction()
loopFunctionInList()