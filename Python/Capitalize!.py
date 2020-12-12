

# Complete the solve function below.
def solve(s):
    li = s.split(" ")
    for i in range(len(li)):
        li[i] = li[i].capitalize()
    return ' '.join(li)
