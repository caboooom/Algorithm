import sys
from collections import deque
input = sys.stdin.readline

# n * n 배열을 모두 0으로 초기화
n = int(input())
board = [[0]*n for _ in range(n)]

# 사과가 있는 자리는 모두 1로 표시
k = int(input())
for k in range(k):
  x, y = map(int,input().split())
  board[x-1][y-1] = 1

# 방향 변경 정보를 입력받아 저장
direction = deque()
l = int(input())
for i in range(l):
  t, d = input().split()
  direction.append((t,d))

# 다음 변경 시간과, 변경 방향
change_t, change_d = direction.popleft()


# 위, 왼, 아래, 오
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 경과시간은 0, 현재방향은 오른쪽으로 초기화
time = 0
direct = 3

# 뱀의 몸이 지나간 좌표를 차례대로 저장
# 꼬리 길이를 줄여야할 때 사용하기 위함
snake = deque()
snake.append((0,0))

x, y = 0, 0
while True:

  # 경과시간을 증가시켜준다.
  time += 1

  # 뱀이 바라보고 있는 좌표로 이동
  nx, ny = x + dx[direct], y + dy[direct]

  # 리스트 범위 벗어나는지 체크
  if 0<=nx<n and 0<=ny<n:
    # 사과가 있으면, 꼬리를 줄이지 않고 이동한다.
    if board[nx][ny] == 1:
      board[nx][ny] = 2
      snake.append((nx,ny))
      x, y = nx, ny
    # 아무것도 없으면, 꼬리를 줄이고 이동한다.
    elif board[nx][ny] == 0:
      tx, ty = snake.popleft()
      board[tx][ty] = 0 # 꼬리가 있던 자리를 0으로
      board[nx][ny] = 2
      snake.append((nx,ny))
      x, y = nx, ny
    # 이동하려는 자리에 자신의 몸이 있으면 종료한다
    elif board[nx][ny] > 1:
      break
  # 이동하려고 하는 좌표가 범위를 벗어나면 종료한다.
  else:
    break

  # 방향을 변경해야 한다면, 변경한다.
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

# 결과 출력
print(time)
      
