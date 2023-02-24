from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,rain):
  if visited[x][y]==1 or graph[x][y]<=rain: #방문할 수 없으면 false리턴
    return False
    
  visited[x][y]=1 #방문처리
  q = deque()
  q.append((x,y))

  while q:
    a, b = q.popleft()

    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      #방문가능하다면
      if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
        visited[nx][ny]=1 #방문처리
        if graph[nx][ny]>rain:
          q.append((nx,ny))
  
  return True

n = int(input())
graph=[]

for i in range(n):
  graph.append(list(map(int,input().split())))

maxH=max(map(max, graph))

result=[]
for rain in range(maxH):
  visited = [[0 for j in range(n)] for i in range(n)]
  cnt=0
  for i in range(n):
    for j in range(n):
      if bfs(i,j,rain)==True:
        cnt+=1
  result.append(cnt)

print(max(result))