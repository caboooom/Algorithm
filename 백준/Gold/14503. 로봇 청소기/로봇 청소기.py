from collections import deque
import sys
input = sys.stdin.readline
 
#반시계회전
rotate=[3,0,1,2]
#후진
backX=[1,0,-1,0]
backY=[0,-1,0,1]
#북,동,남,서쪽 방향
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m = map(int,input().split())
r,c, d = map(int,input().split())
room=[]
for i in range(n):
  room.append(list(map(int,input().split())))

cnt = 0

q=deque()
q.append((r,c))
while q:
  x, y = q.popleft()
  
  if room[x][y]==0:
    cnt += 1
    room[x][y]=2
    
  for i in range(4):
    d=rotate[d]
    nx,ny = x+dx[d], y+dy[d]
    if 0<=nx<n and 0<=ny<m:
      if room[nx][ny]==0:
        room[nx][ny]=2
        cnt += 1
        q.append((nx,ny))
        break

  if len(q)==0:
    nx, ny = x+backX[d], y + backY[d]
    if 0<=nx<n and 0<=ny<m:
      if room[nx][ny]==0:
        room[nx][ny]=2
        cnt +=1
        q.append((nx,ny))
      elif room[nx][ny]==2:
        q.append((nx,ny))
      elif room[nx][ny]==1:
        break

print(cnt)

        
      