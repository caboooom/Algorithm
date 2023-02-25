from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  if graph[x][y]==0:
    return False

  graph[x][y]=1 #방문처리
  q=deque()
  q.append((x,y))

  while q:
    a,b = q.popleft()
    
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
        graph[nx][ny]=0
        q.append((nx,ny))
  return True


  
testNum = int(input())

for test in range(testNum):
  m, n, k = map(int,input().split())
  graph=[[0 for j in range(m)] for i in range(n)]

  for i in range(k):
    b, a = map(int,input().split())
    graph[a][b]=1

  cnt=0
  for i in range(n):
    for j in range(m):
      if bfs(i,j)==True:
        cnt +=1

  print(cnt)