import sys
import heapq
input = sys.stdin.readline
INF=int(1e9)

n, m, k, x = map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  a, b = map(int,input().split())
  graph[a].append((b,1))


def dijkstra(start):
  distance[start]=0
  q=[]
  heapq.heappush(q,(0,start))

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist+i[1]
      if cost < distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(x)

result=[]
for i in range(1,n+1):
  if distance[i]==k:
    result.append(i)

result.sort()

if len(result)>0:
  for i in range(len(result)):
    print(result[i])
else:
  print(-1)