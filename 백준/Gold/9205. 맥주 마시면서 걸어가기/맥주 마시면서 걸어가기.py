import sys
from collections import deque
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
  return abs(x1-x2) + abs(y1-y2)

def bfs(x,y):
  q = deque()
  q.append((x,y))
  visited=[]
  while q:
    a,b=q.popleft()
    if dist(a,b,endX,endY) <= 1000:
      return True
    for i in range(n):
      storeX, storeY = store[i]
      if (storeX, storeY) not in visited:
        if dist(a,b,storeX,storeY) <= 1000:
          visited.append((storeX, storeY))
          q.append((storeX,storeY))
  return False

  
t=int(input())

for _ in range(t):
  n = int(input())
  startX, startY = map(int, input().split())
  store=[]
  for i in range(n):
    x,y = map(int,input().split())
    store.append((x,y))
  endX, endY = map(int, input().split())

  if bfs(startX, startY)==True:
    print('happy')
  else:
    print('sad')

  