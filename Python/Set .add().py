# Enter your code here. Read input from STDIN. Print output to STDOUT
li = []
for i in range(int(input())):
    li.append(input())
print(len(list(set(li))))
