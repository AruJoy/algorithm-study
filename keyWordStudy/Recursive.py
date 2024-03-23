import sys
sys.setrecursionlimit(10**7)

def dividingLine():
    print('''
=====================================================================================
''')


def fact(n):
    if n<=1:
        return 1
    return n * fact(n-1)

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)

def findBiggestPledge(a,b):
    def withLoopFunction(a,b):
        gcd = []
        for i in range(1, min(a,b)):
            if (a%i == 0) & (b%i == 0):
                gcd.append(i)
        print(max(gcd))
    withLoopFunction(a,b)
    dividingLine()
    
    def withEuclideanAndLoop(a,b):
        while b != 0:
            [a, b] = [b, a%b]
        return a
    print(withEuclideanAndLoop(a,b))
    dividingLine()
    
    def withEuclidean(a, b):
        r = b % a
        if r == 0:
            return a
        return withEuclidean(r,b)
    print(withEuclidean(a,b))
    dividingLine()
    return

def fibonacciSequence(k):
    def withLoopFunction(n):
        iter1 = 0
        iter2 = 1
        
        for i in range(1, n, 1):
            result = iter1 + iter2
            iter1 = iter2
            iter2 = result
        return result
    print(withLoopFunction(k))
    dividingLine()
    
    def withRecursive(n):
        if (n <= 1):
            return n
        else: return withRecursive(n-2) + withRecursive(n-1)
    print(withRecursive(k))
    dividingLine()
    return

def hanoi(n):
    source = '1'
    auxiliary = '2'
    target = '3'
    
    def hanoi_recursive(n, source, target, auxiliary):
        print(f'호출 hanoi_recursive({n}, {source}, {target}, {auxiliary})')
        if n == 1:
            print(n, '차 함수 이동')
            print("Move disk 1 from", source, "to", target)
            return
        hanoi_recursive(n - 1, source, auxiliary, target)
        print("Move disk", n, "from", source, "to", target)
        hanoi_recursive(n - 1, auxiliary, target, source)
    hanoi_recursive(n, source, target, auxiliary)


print(fact(7))
dividingLine()

print(sum_n(1000))
dividingLine()

findBiggestPledge(81,27)

fibonacciSequence(10)

hanoi(4)