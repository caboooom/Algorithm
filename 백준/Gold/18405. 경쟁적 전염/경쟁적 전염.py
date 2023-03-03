from collections import deque
import sys
input = sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(q,time): 
  while q:
    virus, s, x, y = q.popleft()
    if s==time:
      return
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<n and 0<=ny<n:
        if graph[nx][ny]==0:
          graph[nx][ny] = virus
          q.append((virus, s+1, nx, ny))
  return
  

n,k = map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

data=[] #바이러스 정보
for i in range(n):
  for j in range(n):
    if graph[i][j]!=0:
      #바이러스 종류, 시간정보, 좌표정보
      data.append((graph[i][j], 0, i, j))

data.sort() #번호가 낮은 종류의 바이러스부터 먼저 증식하므로 정렬해줌
queue = deque(data) #큐에 정렬된 바이러스 정보 삽입

s,a,b=map(int,input().split())

bfs(queue,s)
print(graph[a-1][b-1])
