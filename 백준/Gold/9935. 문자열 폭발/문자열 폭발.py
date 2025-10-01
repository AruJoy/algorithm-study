from sys import stdin
input = stdin.readline
FAILURE = "FRULA"
def explosion(string, trigger):
    length = len(trigger)
    stack = []
    for char in string:
        stack.append(char)
        if len(stack) < length:
            continue
        if "".join(stack[-length:]) == trigger:
            for _ in range(length):
                stack.pop()
    print(FAILURE if len(stack) == 0 else "".join(stack))
    return
def main():
    string = list(input().strip())
    trigger = input().strip()
    explosion(string, trigger)
    return

if __name__ == "__main__":
    main()
