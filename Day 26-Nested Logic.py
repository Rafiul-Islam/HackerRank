# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

ad = input().split()
ed = input().split()

x = datetime.date(int(ad[2]), int(ad[1]), int(ad[0]))
y = datetime.date(int(ed[2]), int(ed[1]), int(ed[0]))
if x > y:
    dd = (x - y)
    if int(ad[1]) == int(ed[1]) and int(ad[2]) == int(ed[2]):
        print(dd.days * 15)
    if int(ad[1]) > int(ed[1]) and int(ad[2]) == int(ed[2]):
        print((int(ad[1]) - int(ed[1])) * 500)
    if int(ad[2]) > int(ed[2]):
        print(10000)
else:
    print(0)
