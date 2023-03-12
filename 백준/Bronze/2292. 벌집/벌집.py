n = int(input())
if n==1 or n==2:
  print(n)
  exit()
  
n -= 2

increase = 2
cur=0
floor=2
while True:
  if n//6<=cur:
    print(floor)
    exit()
  cur += increase
  floor += 1
  increase += 1