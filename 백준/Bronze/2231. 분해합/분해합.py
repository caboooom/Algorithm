n = int(input())

x = 0
while True:
  if x > 1000000 or x > n:
    print(0)
    break
  temp = str(x)
  k = len(temp)
  gn = 0 #generated number
  for i in range(k):
    gn += int(temp[i])
  gn += int(temp)
  if gn == n:
    print(temp)
    break
  x += 1