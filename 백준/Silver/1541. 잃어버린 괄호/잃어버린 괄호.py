from sys import stdin
def parentheses(cities):
    return

input_expression = stdin.readline()

if '-' in input_expression:
    expression = list(input_expression.split('-'))
else: expression = list([input_expression])
    
expressions = list()
for i in range(len(expression)):
    if '+' in expression[i]:
        expressions.append(list(map(int, expression[i].split('+'))))
    else: expressions.append(int(expression[i]))

if type(expressions[0]) == int:
    value = expressions[0]
else: value = sum(expressions[0])

for i in range(1, len(expressions)):
    if type(expressions[i]) == int:
        value -= expressions[i]
    else: value -= sum(expressions[i])

print(value)