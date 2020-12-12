def wrap(string, max_width):
    li = textwrap.wrap(string, max_width)
    for i in range(len(li)-1):
        print(li[i])
    return li[-1]
