import sys
from collections import deque
input = sys.stdin.readline

#n행 m열, 높이가 h
m, n, h = map(int,input().split())


storage=[]

for k in range(h):
  graph = []
  for i in range(n):
    graph.append(list(map(int,input().split())))
  storage.append(graph)

#storage[h][n][m]으로 접근!

q=deque()

for k in range(h):
  for i in range(n):
    for j in range(m):
      if storage[k][i][j]==1:
        q.append((k,i,j))

dz = [0,0,0,0,1,-1]
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
while q:
  c,a,b = q.popleft()
  for i in range(6):
    nc = c+dz[i]
    na = a+dx[i]
    nb = b+dy[i]

    if 0<=nc<h and 0<=na<n and 0<=nb<m:
      if storage[nc][na][nb]==0:
        storage[nc][na][nb] = storage[c][a][b]+1
        q.append((nc,na,nb))

result=0
for k in range(h):
  for i in range(n):
    for j in range(m):
      if storage[k][i][j]==0:
        print(-1)
        exit()
      result = max(result,storage[k][i][j])

print(result-1)