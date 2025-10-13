from sys import stdin
input = stdin.readline
def get_index_list(string):
    m = len(string)
    index_list = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and string[i] != string[j]:
            j = index_list[j - 1]
        if string[i] == string[j]:
            j += 1
            index_list[i] = j
    return index_list
def find_index(original_str, find_str, index_list):
    n, m = len(original_str), len(find_str)
    j = 0
    result = []
    for i in range(n):
        while j > 0 and original_str[i] != find_str[j]:
            j = index_list[j - 1]
        if original_str[i] == find_str[j]:
            if j == m - 1:
                result.append(i - m + 2)
                j = index_list[j]
            else:
                j += 1
    print(len(result))
    print(*result)
    return result
def main():
    original_str = list(input().replace('\n', ''))
    find_str = list(input().replace('\n', ''))
    index_list = get_index_list(find_str)
    find_index(original_str, find_str, index_list)
    return

if __name__ == "__main__":
    main()
