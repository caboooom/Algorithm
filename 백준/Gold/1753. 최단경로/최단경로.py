import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
k = int(input())
graph=[[] for _ in range(v+1)]

for _ in range(e):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

distance = [INF]*(v+1)

#우선순위큐에 출발노드를 삽입
q=[]
heapq.heappush(q,(0,k))
distance[k]=0
#dijkstra
while q:
  dist, cur = heapq.heappop(q)

  if distance[cur] < dist:
    continue
  for i in graph[cur]:
    cost = dist + i[1]
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(q,(cost,i[0]))

#결과 출력
for i in range(1,v+1):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])