from collections import deque
m, n, k = map(int, input().split())

paper = [[0 for j in range(n)] for i in range(m)]
for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(x1,x2):
    for j in range(y1,y2):
      paper[j][i] = 1
visited = [[0 for j in range(n)] for i in range(m)]
dx, dy = [-1,0,1,0], [0,1,0,-1]
def bfs(x,y):
  q = deque([(x,y)])
  paper[x][y]=1
  cnt = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<m and 0<=ny<n and paper[nx][ny]==0:
        q.append((nx,ny))
        paper[nx][ny] = 1
        cnt += 1
  return cnt
answer = []
for i in range(n):
  for j in range(m):
    if visited[j][i]==0 and paper[j][i]==0:
      answer.append(bfs(j,i))
answer.sort()
print(len(answer))
for i in answer:
  print(i,end=' ')