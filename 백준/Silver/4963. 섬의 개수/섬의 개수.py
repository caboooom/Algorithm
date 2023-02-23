import sys
sys.setrecursionlimit(10**6)

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def dfs(x, y):
  if 0 <= x < w and 0 <= y < h and graph[x][y] == 1:
    graph[x][y] = 0  # 방문 처리

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx, ny)
    return True
  return False


while True:
  h, w = map(int, input().split())
  if w == 0 and h == 0:
    break

  graph = []
  for i in range(w):
    graph.append(list(map(int, input().split())))

  cnt = 0
  for i in range(w):
    for j in range(h):
      if dfs(i, j) == True:
        cnt += 1

  print(cnt)
