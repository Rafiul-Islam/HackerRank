if __name__ == '__main__':
    final_list = []
    for i in range(int(input())):
        cmd, *inpt = input().split()
        if cmd == 'append':
            final_list.append(int(inpt[0]))
            # print('append', final_list)
        if cmd == 'pop':
            final_list.pop()
            # print('pop', final_list)
        if cmd == 'sort':
            final_list.sort()
            # print('sort', final_list)
        if cmd == 'reverse':
            final_list.reverse()
            # print('reverse', final_list)
        if cmd == 'print':
            print(final_list)
            # print('print', final_list)
        if cmd == 'insert':
            final_list.insert(int(inpt[0]), int(inpt[1]))
        if cmd == 'remove':
            final_list.remove(int(inpt[0]))
            # print('insert', final_list)
