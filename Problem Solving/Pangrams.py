#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.


def pangrams(s):
    li = []
    for i in s:
        if i.lower() not in li and i != " ":
            li.append(i.lower())
    return 'pangram' if len(li) == 26 else 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
