#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.


def caesarCipher(s, k):
    k = k % 26
    s = list(s)
    for index, value in enumerate(s):
        if value.isupper():
            asci = ord(value)
            asci = asci + k
            if asci > 90:
                asci = (asci - 90) + 65 - 1
            s[index] = chr(asci)

        if value.islower():
            asci = ord(value)
            asci = asci + k
            if asci > 122:
                asci = (asci - 122) + 97 - 1
            s[index] = chr(asci)
    return "".join(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
