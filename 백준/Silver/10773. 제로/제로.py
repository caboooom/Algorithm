import sys 
input = sys.stdin.readline
from collections import deque

q = deque()

n = int(input())
for _ in range(n):
  x = int(input())
  if x != 0:
    q.append(x)
  else:
    q.pop()

print(sum(q))