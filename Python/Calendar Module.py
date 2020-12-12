# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

date = str(input())
day_name = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
day = datetime.datetime.strptime(date, '%m %d %Y').weekday()
print(day_name[day].upper())
