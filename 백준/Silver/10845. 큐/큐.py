import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input())
for _ in range(n):
  command = input().rstrip()
  if "push" in command:
    q.append(int(command.split()[1]))
  elif command == "pop":
    if len(q) == 0:
      print(-1)
    else:
      print(q.popleft())
  elif command == "size":
    print(len(q))
  elif command == "empty":
    print(1) if len(q)==0 else print(0)
  elif command == "front":
    if len(q)>0:
      print(q[0])
    else:
      print(-1)
  elif command == "back":
    if len(q) > 0:
      print(q[-1])
    else:
      print(-1)
      

