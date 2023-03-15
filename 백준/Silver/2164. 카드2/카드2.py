from collections import deque

n = int(input())

if n==1:
  print(1)
  exit()

q=deque()
for i in range(n):
  q.append(i+1)


for i in range(n):
  if len(q)==1:
    print(q.popleft())
    break
  q.popleft()
  q.append(q.popleft())


  