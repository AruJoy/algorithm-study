from sys import stdin

def get_input():
    test_count = int(input().strip())
    test_list = list()
    for i in range(test_count):
        test_list.append(list(map(int, input().split(" "))))
    return test_list
def get_gdc(m1, m2):
    a = max(m1, m2)
    b = min(m1, m2)
    while b != 0:
        a, b = b, a%b
    return a
def extended_gcd(m1:int, m2:int):
    if m2 == 0:
        return (m1, 1, 0)
    g, a, b = extended_gcd(m2, m1%m2)
    return g, b, a - (m1 // m2) * b

def crt(m1:int, m2:int, a1:int, a2:int):
    gdc = get_gdc(m1, m2)
    lcm = m1*m2//gdc
    if (a2 - a1) % gdc != 0:
        print(-1)
        return
    _, x, y = extended_gcd(m1, m2)
    diff = (a2 - a1) // gdc
    t = (diff * x) % (m2 // gdc)
    
    result = (a1 + m1 * t) % lcm
    if result == 0:
        print(lcm)
        return
    print(result)
    return

def solution(test_list: list):
    for test in test_list:
        crt(test[0], test[1], test[2], test[3])
    return

solution(get_input())