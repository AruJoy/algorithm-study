from sys import stdin
input_number = stdin.readline()
input_number = input_number.strip()
if len(input_number) < 2:
    input_number = input_number.zfill(2)
control_Number = 0
count = 0
while control_Number != input_number:
    if count == 0:
        control_Number = input_number
    newNumber = int(input_number[0]) + int(input_number[1])
    newNumber = str(newNumber)
    if len(newNumber) < 2:
        newNumber = newNumber.zfill(2)
    input_number = input_number[1] + str(newNumber[1])
    count += 1
print(count)