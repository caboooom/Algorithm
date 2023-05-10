dx = [0,1,0,-1]
dy = [1,0,-1,0]

n = int(input())
table = [[0 for j in range(n)] for i in range(n)]

target = int(input())

x, y = n//2+1, n//2+1

table[x-1][y-1] = 1


val = 1
for i in range(3,n+1,2): 
  x, y = x-1, y
  for j in range(4):
    if j==0:
      for k in range(i-2):
        val += 1
        table[x-1][y-1]=val
        x += dx[j]
        y += dy[j]
    else:
      for k in range(i-1):
        val += 1
        table[x-1][y-1]=val
        x += dx[j]
        y += dy[j]
  val += 1
  table[x-1][y-1] = val

tx, ty = 0,0
for i in range(n):
  for j in range(n):
    print(table[i][j],end=' ')
    if table[i][j]==target:
      tx,ty = i+1, j+1
  print()

print(tx,ty)
  