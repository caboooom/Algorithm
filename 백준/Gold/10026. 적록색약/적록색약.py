from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs1(x,y):
  if graph[x][y].islower(): #방문한적있으면
    return False

  graph[x][y] = graph[x][y].lower() #방문처리
  q = deque()
  q.append((x,y))

  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      #범위내에 속하고 방문할 수 있고 방문한 적 없는 칸일경우
      if 0<=nx<n and 0<=ny<n and graph[nx][ny]==graph[a][b].upper() and graph[nx][ny].isupper():
        graph[nx][ny] = graph[nx][ny].lower() #방문처리
        q.append((nx,ny))
      
  return True



#입력받기
n = int(input())

graph=[]
for i in range(n):
  arr = []
  temp=input()
  for j in range(n):
    arr.append(temp[j])
  graph.append(arr)


#일반인 결과 출력
cnt1 = 0
for i in range(n):
  for j in range(n):
    if bfs1(i,j)==True:
      cnt1 += 1
print(cnt1,end=' ')

#그래프 비방문처리 & Red와 Green을 같은문자로 통일
for i in range(n):
  for j in range(n):
    graph[i][j] = graph[i][j].upper()
    if graph[i][j] == 'G':
      graph[i][j] = 'R'
    
#적록색약 결과 출력
cnt2 = 0
for i in range(n):
  for j in range(n):
    if bfs1(i,j)==True:
      cnt2 += 1
print(cnt2)
      
