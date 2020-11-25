import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    li = []

    for i in arr:
        li.append(str(i))

    print(" ".join(li[::-1]))
