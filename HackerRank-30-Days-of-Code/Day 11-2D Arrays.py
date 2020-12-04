import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []
    second_row = 0
    three_row = 0
    sum = 0
    sums = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for row in range(4):
        second_row = row + 1
        third_row = row + 2
        for column in range(4):
            sum = arr[row][column] + arr[row][column + 1] + arr[row][column + 2] + arr[second_row][column +
                                                                                                   1] + arr[third_row][column] + arr[third_row][column + 1] + arr[third_row][column + 2]
            sums.append(sum)

    print(max(sums))
