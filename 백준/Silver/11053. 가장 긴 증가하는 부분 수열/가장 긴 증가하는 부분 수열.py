from sys import stdin
def LIS(sequence, length_of_sequence):
    lis_list = list()
    max_val = sequence[0]
    lis_list.append(sequence[0])
    for i in range(1, length_of_sequence):
        if max_val < sequence[i]:
            lis_list.append(sequence[i])
        else:
            for j in range(len(lis_list)):
                if sequence[i] <= lis_list[j]:
                    lis_list[j] = sequence[i]
                    break
        max_val = max(lis_list)
    return len(lis_list)

length_of_sequence = int(stdin.readline())
sequence = list(map(int, stdin.readline().split(' ')))
print(LIS(sequence, length_of_sequence))