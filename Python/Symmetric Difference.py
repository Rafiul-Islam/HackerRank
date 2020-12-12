# Enter your code here. Read input from STDIN. Print output to STDOUT
size1 = int(input())
li1 = list(map(int, input().split()))
size2 = int(input())
li2 = list(map(int, input().split()))
final_list = []
for i in li1:
    if i not in li2 and i not in final_list:
        final_list.append(i)
for i in li2:
    if i not in li1 and i not in final_list:
        final_list.append(i)

final_list.sort()
for i in final_list:
    print(i)
