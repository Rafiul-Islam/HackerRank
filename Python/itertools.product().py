# Enter your code here. Read input from STDIN. Print output to STDOUT
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
final_list = []

for i in range(len(li1)):
    for j in range(len(li2)):
        final_list.append((li1[i], li2[j]))
print(*final_list)
