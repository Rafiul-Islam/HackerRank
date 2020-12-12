# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
details = {}
for i in range(size):
    s = input()
    price = int(s.split(" ")[-1])
    ss = s.split(" ")
    name = " ".join(ss[:len(ss) - 1])
    if name not in details:
        details[name] = price
    else:
        details[name] = details.get(name) + price

for key, value in details.items():
    print(key, value)
