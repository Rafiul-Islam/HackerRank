# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a, b = input().split()
    try:
        a = int(a)
        b = int(b)
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except Exception as e2:
        print("Error Code:", e2)
