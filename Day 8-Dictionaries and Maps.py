import sys

friends = {}
n = float(input())
for i in range(int(n)):
    item = input().split(" ")
    friends[item[0]] = item[1]

query = sys.stdin.readline().strip()

while query:
    if query in friends:
        print(f"{query}={friends[query]}")
    else:
        print("Not found")
    query = sys.stdin.readline().strip()
