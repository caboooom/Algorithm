#풀이참고
#https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def tomato():

  while q:
    x,y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        q.append((nx,ny))
  return


#입력받기
  
m,n = map(int,input().split())

graph=[]
for i in range(n):
  temp = list(map(int,input().split()))
  graph.append(temp)


#토마토 익히기 과정 실시!

q = deque()
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      q.append((i,j))

tomato()

#정답 출력
ans=0
for i in range(n):
  for j in range(m):
    #안 익은 토마토가 하나라도 존재하면 -1을 출력하고 종료
    if graph[i][j] == 0:
      print(-1)
      exit(0)
    if graph[i][j]>ans:
      ans = graph[i][j]

print(ans-1)
