# Enter your code here. Read input from STDIN. Print output to STDOUT
total_shoes = int(input())
shoes_size = list(map(int, input().split()))
total_customers = int(input())
total = 0
for i in range(total_customers):
    size, prize = input().split()
    if int(size) in shoes_size:
        total += int(prize)
        shoes_size.remove(int(size))

print(total)
