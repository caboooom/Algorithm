
n = int(input())
table = [[0 for j in range(n)] for i in range(n)]

target = int(input())


#1**2 회
#3**2 - 1회
#5**2 - 1회

#3이면 1, 5면3 , 7이면4

x, y = n//2+1, n//2+1
if n == 3:
  x, y = 1, 1
table[x-1][y-1] = 1
#print(x,y)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

if n == 3:
  temp = [[9,2,3],[8,1,4],[7,6,5]]
  print("9 2 3")
  print("8 1 4")
  print("7 6 5")
  for i in range(3):
    for j in range(3):
      if temp[i][j] == target:
        print(i+1,j+1)
        exit()

val = 1
for i in range(3,n+1,2): #n까지 해도 대나?
  #3일때는 +2, +2, +2 , +2
  #5일때는 +4, +4, +4, +4
  x, y = x-1, y
  #print(x,y)
  for j in range(4):
    if j==0:
      for k in range(i-2):
        val += 1
        #print(x,y,val)
        table[x-1][y-1]=val
        x += dx[j]
        y += dy[j]
    else:
      for k in range(i-1):
        val += 1
        #print(x,y,val)
        table[x-1][y-1]=val
        x += dx[j]
        y += dy[j]
  val += 1
  table[x-1][y-1] = val
     # table[x][y] = val
#table[0][0] = val+1
#print(table)

tx, ty = 0,0
for i in range(n):
  for j in range(n):
    print(table[i][j],end=' ')
    if table[i][j]==target:
      tx,ty = i+1, j+1
  print()

print(tx,ty)


      
    
    
  