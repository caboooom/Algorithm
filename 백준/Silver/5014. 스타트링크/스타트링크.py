from collections import deque

f, s, g, u, d = map(int, input().split())

elevator = [0 for _ in range(f+1)]
q = deque()
q.append(s)
elevator[s] = 1

if s == g:
  print(0)
  exit(0)

while q:
  cur = q.popleft()
  if cur == g:
    break
  for i in (u, -d):
    next = cur + i
    if 0 < next <= f and elevator[next] == 0:
      elevator[next] = elevator[cur] + 1
      q.append(next)

if elevator[g] == 0:
  print("use the stairs")
else:
  print(elevator[g]-1)