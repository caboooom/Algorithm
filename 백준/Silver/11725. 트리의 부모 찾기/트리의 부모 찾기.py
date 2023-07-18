import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]

q = deque()
q.append(1)
visited[1] = 1
while q:
  parent = q.popleft()
  for i in range(len(graph[parent])):
    child = graph[parent][i]
    if visited[child] == 0:
      result[child] = parent
      visited[child] = 1
      q.append(child)

for i in range(2,n+1):
  print(result[i])