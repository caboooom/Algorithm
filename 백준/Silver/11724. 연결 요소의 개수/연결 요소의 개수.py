from collections import deque
import sys

def bfs(x):
  if visited[x]==1:
    return False
  visited[x]=1 #방문 처리
  q = deque()
  q.append(x)

  while q:
    cur = q.popleft()
    for i in range(len(graph[cur])):
      next = graph[cur][i]
      if visited[next]==0:
        visited[next]=1 #방문처리
        q.append(next)
  return True

#그래프 정보 입력받기
n,m = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
  a,b=map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)


visited = [0]*(n+1)

#연결요소 개수 카운트하기
cnt=0
for i in range(1,n+1):
  if bfs(i)==True:
    cnt += 1
print(cnt)