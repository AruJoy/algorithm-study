from sys import stdin
inputInformation = stdin.readline()
inputInformation = inputInformation.split(' ')

rangeLength = int(inputInformation[2])
numberOfAnimals = int(inputInformation[1])
animals = list()

gunPorts = stdin.readline()
gunPorts = gunPorts.split(' ')
gunPorts.sort()

for i in range(len(gunPorts)):
    gunPorts[i] = int(gunPorts[i])

for i in range(numberOfAnimals):
    inputValue = stdin.readline()
    inputValue = inputValue.split(' ')
    animals.append([int(inputValue[0]), int(inputValue[1])])


def isKilledInRange(animal,length):
    x1 = animal[0] - length + animal[1]
    x2 = animal[0] + length - animal[1]
    return[x1, x2]

def isKilled(dangerZone, gunPorts):
    left = 0
    right = len(gunPorts)-1
    while left <=right:
        mid = (left + right) // 2

        if dangerZone[0] <= gunPorts[mid] <= dangerZone[1]:
            return True
        elif gunPorts[mid] < dangerZone[0]:
            left = mid + 1
        elif dangerZone[1] < gunPorts[mid]:
            right = mid - 1
    return False

def numberOfKilledAnimals(animals, gunPorts, length):
    count = 0
    for animal in animals:
        if animal[1] > length:
            continue
        dangerZone = isKilledInRange(animal, length)
        if isKilled(dangerZone, gunPorts):
            count += 1
    return count

print(numberOfKilledAnimals(animals, gunPorts, rangeLength))