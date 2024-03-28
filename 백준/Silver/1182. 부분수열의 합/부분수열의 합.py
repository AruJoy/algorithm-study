from sys import stdin
input_conditions = stdin.readline()
input_conditions = input_conditions.split(' ')
input_matrix = stdin.readline()
input_matrix = input_matrix.split(' ')
for i in range(len(input_matrix)):
    input_matrix[i] = int(input_matrix[i])

matrix_size = int(input_conditions[0])
target_value = int(input_conditions[1])
count = 0

sub_matrix = []

def find_sub_matrix(input_matrix, sub_matrix, sub_matrix_size, first_element_pointer):
    global count
    global target_value
    if sub_matrix_size > matrix_size:
        return
    if sum(sub_matrix) == target_value and len(sub_matrix)!= 0:
        count += 1
    sub_matrix_size = 0
    
    
    for i in range(first_element_pointer, len(input_matrix)):
        sub_matrix.append(input_matrix[first_element_pointer])
        find_sub_matrix(input_matrix,sub_matrix ,sub_matrix_size + 1, first_element_pointer + 1)
        sub_matrix.pop()
        first_element_pointer += 1
find_sub_matrix(input_matrix, sub_matrix, 0, 0)
print(count)


# 이진수 목록 = combination