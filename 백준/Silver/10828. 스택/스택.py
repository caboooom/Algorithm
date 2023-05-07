import sys
from collections import deque
input = sys.stdin.readline

stack = deque()
n = int(input())
for _ in range(n):
  command = input().rstrip()
  if "push" in command:
    stack.append(int(command.split()[1]))
  elif command == "pop":
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif command == "size":
    print(len(stack))
  elif command == "empty":
    print(1) if len(stack)==0 else print(0)
  elif command == "top":
    if len(stack)>0:
      print(stack[-1])
    else:
      print(-1)
      

