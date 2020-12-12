li_size, target_list_size = input().split()
li_size = int(li_size)
target_list_size = int(target_list_size)
li = []
target = []
for i in range(li_size):
    li.append(input())
for i in range(target_list_size):
    target.append(input())
for i in range(target_list_size):
    count_list = []
    if target[i] in li:
        for index, value in enumerate(li):
            if target[i] == value:
                count_list.append(index + 1)
        print(*count_list)
    else:
        print(-1)
