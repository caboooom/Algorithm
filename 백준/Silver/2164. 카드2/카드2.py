from collections import deque

n = int(input())

q=deque()
for i in range(n):
  q.append(i+1)

for i in range(n):
  if len(q)==1:
    print(q.popleft())
    break
  q.popleft()
  q.append(q.popleft())


  