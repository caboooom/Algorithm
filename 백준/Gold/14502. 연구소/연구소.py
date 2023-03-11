from itertools import combinations
from collections import deque
import sys 
input = sys.stdin.readline

n,m = map(int,input().split())
arr=[]
for i in range(n):
  arr.append(list(map(int,input().split())))

zero=[]
for i in range(n):
  for j in range(m):
    if arr[i][j]==0:
      zero.append((i,j))
combi = list(combinations(zero,3))

answer=0
q=deque()
dx,dy = [-1,1,0,0],[0,0,1,-1]
arr2=[[0]*m for _ in range(n)]
for c in range(len(combi)):
  for i in range(n):
    for j in range(m):
      arr2[i][j]=arr[i][j]
      if arr[i][j]==2:
        q.append((i,j))
  p1,p2,p3=combi[c]
  #벽세우기
  arr2[p1[0]][p1[1]]=1
  arr2[p2[0]][p2[1]]=1
  arr2[p3[0]][p3[1]]=1

  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and arr2[nx][ny]==0:
        arr2[nx][ny]=2
        q.append((nx,ny))

  #안전영역 세기
  cnt=0
  for i in range(n):
    for j in range(m):
      if arr2[i][j]==0:
        cnt+=1
  answer = max(answer,cnt)

print(answer)