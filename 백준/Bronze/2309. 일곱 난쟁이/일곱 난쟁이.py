from sys import stdin

dwarfs = [int(stdin.readline()) for i in range(9)]
hights = sum(dwarfs)
criminal = hights - 100
def findCriminal():
    for i in range(len(dwarfs)):
        for j in range(i+1, len(dwarfs)):
            if dwarfs[i] + dwarfs[j] == criminal:
                dwarfs.remove(dwarfs[j])
                dwarfs.remove(dwarfs[i])
                return
findCriminal()
dwarfs.sort()
for i in dwarfs:
    print(i)