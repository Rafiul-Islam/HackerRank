import math


def check_primality(element):
    count = 0
    if element == 1:
        return False
    if element % 2 == 0 and element > 2:
        return False
    for i in range(2, int(math.sqrt(element)) + 1):
        if element % i == 0:
            return False
    return True


n = int(input())
elements = []
for i in range(n):
    elements.append(int(input()))
for i in elements:
    print('Prime' if check_primality(i) else 'Not prime')
