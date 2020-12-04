# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
li = []
for i in range(0, n):
    li.append(input())

for i in li:
    print("".join(i[::2]), "".join(i[1::2]))
