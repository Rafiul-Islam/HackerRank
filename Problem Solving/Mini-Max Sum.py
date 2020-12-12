#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    sum_list = []
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            if j == i:
                continue
            sum += arr[j]
        sum_list.append(sum)
    print(min(sum_list), max(sum_list))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
