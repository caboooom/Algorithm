
month, day = map(int,input().split())

months = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

target = sum(days[:month]) + day-1

print(months[target%7])