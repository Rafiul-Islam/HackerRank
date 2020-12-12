import math

marks = []
size = int(input())
title = list(map(str, input().split()))
index_of_mark = title.index('MARKS')
for i in range(size):
    marks.append(int(input().split()[index_of_mark]))
print('%.2f' % (math.fsum(marks) / len(marks)))
