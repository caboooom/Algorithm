import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def bfs(x,y):
  q = deque()
  q.append((x,y))
  cnt = 0
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
        q.append((nx,ny))
        paper[nx][ny] = 2 # 방문표시
        cnt += 1
  return cnt if cnt>0 else 1
        
n, m = map(int, input().split())
paper = []
for _ in range(n):
  paper.append(list(map(int,input().split())))

count = 0
area = 0
for i in range(n):
  for j in range(m):
    if paper[i][j] == 1:
      count += 1
      area = max(area, bfs(i,j))
print(count)
print(area)