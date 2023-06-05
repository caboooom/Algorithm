from collections import deque
import sys
input = sys.stdin.readline

deq = deque()

n = int(input())
for _ in range(n):
  cmd = input().split()
  if cmd[0] == 'push_front':
    deq.appendleft(int(cmd[1]))
  elif cmd[0] == 'push_back':
    deq.append(int(cmd[1]))
  elif cmd[0] == 'pop_front':
    try:
      print(deq.popleft())
    except:
      print(-1)
  elif cmd[0] == 'pop_back':
    try:
      print(deq.pop())
    except:
      print(-1)
  elif cmd[0] == 'size':
    print(len(deq))
  elif cmd[0] == 'empty':
    if len(deq)==0:
      print(1)
    else:
      print(0)
  elif cmd[0] == 'front':
    try:
      print(deq[0])
    except:
      print(-1)
  elif cmd[0] == 'back':
    try:
      print(deq[-1])
    except:
      print(-1)
      