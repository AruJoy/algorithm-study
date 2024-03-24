from sys import stdin
input = stdin.readline()
a,b = input.split(' ')
a= int(a)
b= int(b)

print(f'''{a+b}
{a-b}
{a*b}
{a//b}
{a%b}
''')