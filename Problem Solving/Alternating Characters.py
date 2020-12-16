#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.


def alternatingCharacters(s):
    s = list(s)
    count = 1
    deletion_count = 0
    for i in range(len(s)):
        if len(s) > count and s[count - 1] == s[count]:
            del s[count]
            deletion_count += 1
        else:
            count += 1
    return deletion_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
