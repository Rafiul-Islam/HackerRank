#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    length_difference = 6 - n
    number_check = False
    lower_case_check = False
    upper_case_check = False
    special_characters_check = False
    count = 4

    for i in password:
        if i in numbers:
            number_check = True
        if i in lower_case:
            lower_case_check = True
        if i in upper_case:
            upper_case_check = True
        if i in special_characters:
            special_characters_check = True

    count -= 1 if number_check else 0
    count -= 1 if lower_case_check else 0
    count -= 1 if upper_case_check else 0
    count -= 1 if special_characters_check else 0

    return length_difference if length_difference > count else count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
