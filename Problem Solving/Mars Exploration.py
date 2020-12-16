#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.


def marsExploration(s):
    length = len(s)
    total_sos = length // 3
    others = length % 3
    org_signal = 'SOS' * total_sos + 'SOS'[:others]
    count = 0
    for i in range(length):
        if s[i] != org_signal[i]:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
