from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append( list(map(int, input().split())) )

visited = [[0 for _ in range(m)] for _ in range(n)]


answer = 0

def bfs(x,y):
  q = deque()
  q.append((x,y))
  visited[x][y] = 1
  dx, dy = [-1,0,1,0], [0,1,0,-1]
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny]>0:
        visited[nx][ny] = 1
        q.append((nx,ny))

# 빙산이 한덩어리인지 체크
def check():
  # visited 초기화
  for i in range(n):
    for j in range(m):
      visited[i][j] = 0
  cnt = 0
  for i in range(n):
    for j in range(m):
      if arr[i][j] != 0 and visited[i][j] == 0:
        bfs(i,j)
        cnt += 1
  return cnt

q = deque()

def melt(x,y):
  # 방문배열 초기화
  for i in range(n):
    for j in range(m):
      visited[i][j] = 0

  q.append((x,y))
  visited[x][y] = 1

  dx = [-1,0,1,0]
  dy = [0,1,0,-1]

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0 and arr[x][y]>0:
      arr[x][y] -= 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny]>0:
        visited[nx][ny] = 1
        for j in range(4):
          tx, ty = nx + dx[j], ny + dy[j]
          if 0 <= tx < n and 0 <= ty < m and not visited[tx][ty] and arr[tx][ty]==0:
            if arr[nx][ny] > 0:
              arr[nx][ny] -= 1
        q.append((nx,ny))
  

while True:

  # 빙산이 몇덩어리인지 체크
  if check() > 1:
    print(answer)
    break

  # 빙산 녹는 작업
  flag = False
  for i in range(n):
    for j in range(m):
      if arr[i][j] > 0:
        melt(i,j)
        flag = True
        break
    if flag:
      break
  answer += 1 # 1년 추가

  # 빙산이 다 녹았는지 체크
  flag = False
  for i in range(n):
    for j in range(m):
      if arr[i][j] != 0:
        flag = True
        break
    if flag:
      break
  if flag == False:
    print(0)
    break