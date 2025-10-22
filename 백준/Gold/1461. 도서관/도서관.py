from sys import stdin
input = stdin.readline


def get_longest_length(books, n_carry):
    i = 0
    if abs(books[0]) > abs(books[-1]):
        ans = abs(books[0])
        while books and books[0] < 0 and i < n_carry:
            books.pop(0)
            i += 1
        return ans
    ans = abs(books[-1])
    while books and books[-1] > 0 and i < n_carry:
        books.pop()
        i += 1
    return ans


def main():
    _, n_carry = map(int, input().split())
    books = list(map(int, input().split()))

    books.sort()
    ans = get_longest_length(books, n_carry)
    while books and books[0] < 0:
        i = 0
        ans -= books[0] * 2
        while books and books[0] < 0 and i < n_carry:
            books.pop(0)
            i += 1

    while books:
        i = 0
        ans += books[-1] * 2
        while books and i < n_carry:
            books.pop()
            i += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
