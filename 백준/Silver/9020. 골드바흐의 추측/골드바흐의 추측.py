from sys import stdin
num_inputs = stdin.readline()
num_inputs = int(num_inputs)
inputList = list()

for i in range(num_inputs):
    inputList.append(int(stdin.readline()))

primeList = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
def isPrime(number, primeList):
    if number % 2 == 0 and number !=2 :
        return False
    if number == 1:
        return False
    if number in primeList:
        return True
    for prime in primeList:
        if number % prime == 0:
            return False
    return True

def printAnswer(primeList, number):
    checkRange = number // 2
    for i in range(checkRange):
        value = checkRange - i
        if isPrime(value, primeList) and isPrime(number - value, primeList):
            print(f'{value} {number - value}')
            return

for i in inputList:
    printAnswer(primeList, i)