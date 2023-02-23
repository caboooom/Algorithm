import sys
from collections import deque

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def bfs(x,y):
  if graph[x][y]==0: #이미 방문한 적 있으면 false리턴
    return False
    
  graph[x][y]=0 #방문 처리
  q=deque()
  q.append((x,y))

  while q:
    a,b=q.popleft()
    for i in range(8):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<w and 0<=ny<h and graph[nx][ny]==1:
        graph[nx][ny]=0
        q.append((nx,ny))
  return True #인접한 칸들 모두 방문이 끝나면 true리턴

while True:
  h, w = map(int, input().split())
  if w == 0 and h == 0:
    break

  graph = []
  for i in range(w):
    graph.append(list(map(int, input().split())))

  cnt = 0
  for i in range(w):
    for j in range(h):
      if bfs(i, j) == True:
        cnt += 1

  print(cnt)
