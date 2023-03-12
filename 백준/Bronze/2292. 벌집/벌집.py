n=int(input())

floor = 1
cur=1
while n>cur:
  cur += floor*6
  floor += 1
print(floor)