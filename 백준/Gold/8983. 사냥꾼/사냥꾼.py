from sys import stdin
M, numberOfAnimals, rangeLength  = map(int, stdin.readline().split())
gunPorts = list(map(int, stdin.readline().split()))
animals = [list(map(int, stdin.readline().split())) for i in range(numberOfAnimals)]
count = 0

gunPorts.sort()

for animal in animals:
    if animal[1] > rangeLength:
        continue
    x1 = animal[0] - rangeLength + animal[1]
    x2 = animal[0] + rangeLength - animal[1]
    
    left = 0
    right = len(gunPorts)-1
    while left <= right:
        mid = (left + right) //2 
        if x1 <= gunPorts[mid] <= x2:
            count += 1
            break
        elif gunPorts[mid] < x1:
            left = mid + 1
        else:
            right = mid - 1

print(count)
