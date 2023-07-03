import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
table = []
for _ in range(n):
  table.append( list(map(int,input().split())) )

visited = [[0 for j in range(m)] for i in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
  q = deque()
  q.append((x,y))

  visited[x][y] = 1
  
  while q:
    x,y = q.popleft()
      
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
        if table[nx][ny] == 0:
          visited[nx][ny] = 1
        elif table[nx][ny] == 1:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx,ny))

for i in range(n):
  for j in range(m):
    if table[i][j] == 2:
      bfs(i,j)

for i in range(n):
  for j in range(m):
    if table[i][j] == 0:
      print(0,end=' ')
    else:
      print(visited[i][j]-1, end=' ')
  print()