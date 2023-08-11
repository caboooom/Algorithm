import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

cur = sum(visitors[:x])
max_visitors = cur
days = 1

for i in range(1,n-x+1):
  
  cur -= visitors[i-1]
  cur += visitors[i+x-1]
  if cur > max_visitors:
    max_visitors = cur
    days = 1
  elif cur == max_visitors:
    days += 1

if max_visitors == 0:
  print("SAD")
else:
  print(max_visitors)
  print(days)