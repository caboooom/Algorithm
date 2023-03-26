import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0]*n for _ in range(n)]

# 사과
for k in range(k):
  x, y = map(int,input().split())
  board[x-1][y-1] = 1

direction = deque()
l = int(input())
for i in range(l):
  t, d = input().split()
  direction.append((t,d))

change_t, change_d = direction.popleft()


# 위, 왼, 아래, 오
dx = [-1,0,1,0]
dy = [0,-1,0,1]

time = 0
direct = 3

board[0][0] = 2
snake = deque()
snake.append((0,0))
x, y = 0, 0
while True:
  time += 1

  # 이동
  nx, ny = x + dx[direct], y + dy[direct]
  
  if 0<=nx<n and 0<=ny<n:
    if board[nx][ny] == 1:
      board[nx][ny] = 2
      snake.append((nx,ny))
      x, y = nx, ny
    elif board[nx][ny] == 0:
      tx, ty = snake.popleft()
      board[tx][ty] = 0
      board[nx][ny] = 2
      snake.append((nx,ny))
      x, y = nx, ny
    elif board[nx][ny] > 1:
      break
  else:
    break

  # 방향 변경
  if time == int(change_t):
    if change_d == 'D':
      if direct > 0:
        direct -= 1
      else:
        direct = 3
    elif change_d == 'L':
      if direct < 3:
        direct += 1
      else:
        direct =0
    if len(direction) > 0:
      change_t, change_d = direction.popleft()
    else:
      change_t = 0
print(time)
      
