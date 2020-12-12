if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score
    students = dict(sorted(students.items(), key=lambda item: item[1]))
    second_key = 0
    value_list = []
    for key, value in students.items():
        value_list.append(value)

    value_list = list(set(value_list))
    value_list.sort()
    second_key = value_list[1]
    final_list = []
    for key, value in students.items():
        if value == second_key:
            final_list.append(key)

    final_list.sort()
    for i in final_list:
        print(i)
