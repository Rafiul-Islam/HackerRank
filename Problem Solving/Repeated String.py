#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    l = len(s)
    m, k = n // l, n % l
    a_in_s = s.count('a')
    if k != 0:
        t = a_in_s * m + s[:k].count('a')
    else:
        t = a_in_s * m
    return t


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
