n = int(input())
table = [[0 for j in range(n)] for i in range(n)]

target = int(input())

# 정가운데 좌표 구하기
x, y = n//2+1, n//2+1
# 1을 채워넣기
val = 1
table[x-1][y-1] = val

# 오른쪽, 아래, 왼쪽, 위
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 한 껍데기씩 채워넣기
for i in range(3,n+1,2):
  # 출발좌표로 이동 (왼쪽 대각선)
  x, y = x-1, y-1
  # 오른쪽 - 아래 - 왼쪽 - 위 순서대로
  for j in range(4):
    # 각각 n-1칸씩 채우기
    for k in range(i-1):
      val += 1        
      x += dx[j]
      y += dy[j]
      table[x-1][y-1]=val

# 결과 출력
tx, ty = 0,0
for i in range(n):
  for j in range(n):
    print(table[i][j],end=' ')
    if table[i][j]==target:
      tx,ty = i+1, j+1
  print()
  
print(tx,ty)