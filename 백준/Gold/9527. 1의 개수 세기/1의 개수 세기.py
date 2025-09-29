from sys import stdin
input = stdin.readline
INF = float('INF')

def count(value):
    count = 0
    bit = 1
    while bit <= value:
        cycle = bit << 1
        count += (value//cycle)*bit
        count += max(0, value%cycle - bit + 1)
        bit = bit << 1
    return count
def main():
    a, b = map(int, input().split())
    print(count(b) - count(a-1))
    return

if __name__ == "__main__":
    main()
