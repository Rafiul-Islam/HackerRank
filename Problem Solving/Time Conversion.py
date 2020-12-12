#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    t = s[-2] + s[-1]
    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]

    if t == 'PM' and hour != '12':
        hour = int(hour) + 12
        hour = str(hour)

    if t == 'AM' and hour == '12':
        hour = '00'

    if len(hour) == 1:
        hour == '0' + str(hour)

    return hour + ":" + minute + ":" + second


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
