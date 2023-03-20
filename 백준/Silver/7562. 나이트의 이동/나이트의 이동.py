from collections import deque

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

test = int(input())
for _ in range(test):
  l = int(input())
  start_x, start_y = map(int,input().split())
  end_x, end_y = map(int,input().split())

  board = [[0]*l for i in range(l)]
  q=deque()
  q.append((start_x,start_y))
    
  while q:
    x, y = q.popleft()
    if x==end_x and y==end_y:
      break
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<l and 0<=ny<l and board[nx][ny]==0:
        board[nx][ny] = board[x][y] + 1
        q.append((nx,ny))

  print(board[x][y])