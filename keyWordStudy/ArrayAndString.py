def dividingLine():
    print('''
=====================================================================================
''')

def multiDimensionalArray():
    n=5
    arr1 = [[0 for j in range(n)] for i in range(n)]
    arr2 = [[0] * n] * n
    arr3 = [[0] * n for i in range(n)]
    
    print(arr1)
    print(arr2)
    print(arr3)
    
    dividingLine()
    
    arr1[1][2] = 3
    arr2[1][2] = 3
    arr3[1][2] = 3
    
    print(arr1)
    print(arr2)
    print(arr3)

def oneDimensionalArray():
    n=5
    arr1 = [0 for i in range(n)]
    arr2 = [0] * n 
    
    print(arr1)
    print(arr2)
    
    dividingLine()
    
    arr1[2] = 3
    arr2[2] = 3
    
    print(arr1)
    print(arr2)
    
    arr3 = [[] for i in range(n)]
    arr4 =  [[]] * n
    
    arr3[2].append(3)
    arr4[2].append(3)
    
    print(arr3)
    print(arr4)
    
    dividingLine()

def string():
    a = 'abcdefg'
    b = '123456'
    c = '''오늘의
    코딩
    공부
    '''
    
    print(a[0])
    print(a[-1])
    print(a[1:4])
    print(a[-3:])


    print(len("krafton jungle"))
    
    s1 = "krafton"
    s2 = "jungle"
    print(s1+s2)
    
    dividingLine()
    
    num = '123'
    integer = int(num)
    f = float(num)
    
    dividingLine()
    
    words = ['amazon', "Krafton", "JUNGLE"]
    
    for w in words:
        print (f'result for {w} is lower', w.islower())
    
    for w in words:
        print (f'result for {w} is lower', w.isupper())
    
    dividingLine()
    
    stringSample = 'hi jungle this is SampleStringLine'
    conversionTest = stringSample
    print(stringSample)
    print(conversionTest.upper())
    print(conversionTest.lower())
    print(stringSample.capitalize())
    print(stringSample.title())
    
    stringSample = '    hi jungle   '
    print(stringSample.lstrip())
    stringSample = '    hi jungle   '
    print(stringSample.rstrip())
    stringSample = '    hi jungle   '
    print(stringSample.strip())
    stringSample = '    hi jungle   '
    print(stringSample.strip('jungle    '))
    
    dividingLine()
    
    just = 'just & center'
    print(just.ljust(20))
    
    just = 'just & center'
    print(just.rjust(20))
    
    just = 'just & center'
    print(just.rjust(20,'X'))
    
    just = 'just & center'
    print(just.center(20))
    
    just = 'just & center'
    print(just.center(20,'X'))
    
    dividingLine()
    
    priceList = list()
    price = 'monster', '2300'
    priceList.append(price)
    price = 'orange juice', '2000'
    priceList.append(price)
    price = 'water', '900'
    priceList.append(price)
    
    for price in priceList:
        print(price[0], '  |  ', price[1])
        
    for price in priceList:
        print(price[0].ljust(15), '|', price[1].zfill(5))
    
    for price in priceList:
        print(price[0].ljust(15), '|', price[1].rjust(9))
    
    dividingLine()
    
    password = 'wwwwbwwwawwwnwwwawwwnwwaww'
    print(password.replace('w', 'k'))
    print(password.replace('w', '', 5))
    print(password.replace('w', ''))
    
    dividingLine()

    sentence = '{} is {} and {} is {}'
    print(sentence.format('Knowledge', 'power', 'France', 'bacon'))
    sentence = sentence+"{}"
    print(sentence)
    sentence = sentence.format('Knowledge', 'power', 'France', 'bacon', '.')
    print(sentence)
    
    dividingLine()
    
    print(sentence.find('power'))
    
    print(sentence.split())
    print(sentence.split('is'))
    
    dividingLine()
    print(",".join(["abc","def","ghi"]))
    print("XXX".join(["abc","def","ghi"]))

multiDimensionalArray()

oneDimensionalArray()

string()