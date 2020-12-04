#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numberOfSwaps = 0
for i in range(n):
    for j in range(0, (n - 1)):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numberOfSwaps += 1
    if (numberOfSwaps == 0):
        break
print(f"Array is sorted in {numberOfSwaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[len(a)-1]}")
